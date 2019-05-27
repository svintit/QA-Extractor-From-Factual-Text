import ast
import inspect
import os
import random

import en_core_web_sm

from .q_dicts import advanced_q_dict
from .q_dicts import n_chunk_q_dict


parent_dir = os.path.dirname(
    os.path.dirname(
        os.path.abspath(
            inspect.getfile(
                inspect.currentframe()
            )
        )
    )
)


class OpenFiles:
    def open_output_file():
        out = open(parent_dir + '/extractor_app/static/'
                   'extractor/output/extractor.output', 'a')
        out.seek(0)
        out.truncate()  # Empty file on open as append mode needed
        return out


class ProcessInput:
    nlp = en_core_web_sm.load()

    def __init__(self, input_):
        self.input_ = input_

    # Tokenise sentence
    def tok_sent(self):
        return self.nlp(self.input_).sents

    # Get SpaCy doc
    def get_nlp_doc(self, sent):
        return self.nlp(str(sent))

    # Get part of speech tags
    def pos_tag(self, sent_doc):
        pos_tagged = [[tok.text, tok.pos_] for tok in sent_doc]
        return pos_tagged

    # Get noun chunks
    def n_chunk(self, sent_doc):
        chunks = [[chunk.text, chunk.root.head.text]
                  for chunk in sent_doc.noun_chunks]
        return chunks


class QuestionCreator:
    def __init__(self, input_, answer_):
        self.input_ = input_
        self.answer_ = answer_

    def advanced_q(self, pos_tagged):
        POS_LIST = [
            'VERB', 'ADV', 'CCONJ', 'DET',
            'ADJ', 'NOUN', 'ADP',
            'PROPN', 'PART', 'NUM', 'PROPN'
        ]

        q_list = []
        extracted = ''
        wh_object = 'who'

        for X in self.input_.ents:
            if pos_tagged[0][0] in str(X):
                if str(X.label_) == "ORG":
                    wh_object = "what"

            if advanced_q_dict.get(X.label_) is not None:
                questions = advanced_q_dict.get(X.label_)

                for i, tup in enumerate(pos_tagged):
                    if extracted != '':
                        if tup[1] in POS_LIST \
                           and extracted.split()[-1] == pos_tagged[i - 1][0]:
                            extracted += ' ' + str(tup[0])
                    else:
                        if tup[1] == POS_LIST[0] \
                           and pos_tagged[i - 1][0] != 'I':
                            if tup[0][0].isupper():
                                tup[0] = 'was ' + tup[0].lower()
                            extracted = str(tup[0])

                if extracted != '' and len(extracted.split()) > 2:
                    q_list = [q.replace('{EXTRACTED}', extracted)
                              .replace('{WH}', wh_object)
                              for q in questions]
        return q_list

    def n_chunk_q(self, noun_chunks, q_size):
        q_list = []
        used_ents = []

        for X in self.input_.ents:
            if n_chunk_q_dict.get(X.label_) is not None \
               and str(X) not in used_ents:
                used_ents.append(str(X))
                questions = n_chunk_q_dict.get(X.label_)
                questions = [questions[random.randrange(len(questions))]]

                n_chunk = [chunk[1] for chunk in noun_chunks
                           if chunk[0] == X.text]

                if n_chunk != []:
                    q_list += [q.replace('{VERB}', n_chunk[0].lower()).replace
                               ('{ENT}', X.text)
                               for q in questions]
                else:
                    if X.label_ == "DATE":
                        if X.text[-1] == 's':
                            n_chunk = 'are'
                        else:
                            n_chunk = 'in'
                    else:
                        n_chunk = 'is'

                    q_list += [q.replace('{VERB}', n_chunk).replace
                               ('{ENT}', X.text)
                               for q in questions]
        return q_list

    def q_decider(self, q_list, q_size):
        decided_list = []

        if len(q_list) > 1:
            while len(decided_list) < q_size and len(q_list) > 0:
                chosen = q_list[random.randrange(len(q_list))]
                decided_list.append(chosen)
                q_list.remove(chosen)
        else:
            decided_list = q_list

        return decided_list

    def final_q_list(self):
        process_input = ProcessInput(self.input_)
        sentences = process_input.tok_sent()

        total_q_list = []
        used_q = []
        printed = True

        for sent in sentences:
            # Do not output questions for sentences that are questions.
            if '?' in str(sent):
                pass

            doc = process_input.get_nlp_doc(sent)

            # Retrieve advanced questions
            pos_tagged = process_input.pos_tag(doc)
            advanced_q_list = (
                QuestionCreator(doc, sent)
                .advanced_q(pos_tagged)
            )
            revised_advanced_list = (
                QuestionCreator(doc, sent)
                .q_decider(advanced_q_list, 1)
            )

            # Output more questions if previous function returns none
            if len(revised_advanced_list) < 2:
                q_size = 3
            else:
                q_size = 2

            # Output more questions based on length of answer.
            if len(str(sent)) > 200:
                q_size += 1

            # Retrieve noun chunk questions
            noun_chunks = process_input.n_chunk(doc)
            noun_q_list = (
                QuestionCreator(doc, sent)
                .n_chunk_q(noun_chunks, q_size)
            )
            revised_noun_list = (
                QuestionCreator(doc, sent)
                .q_decider(noun_q_list, q_size)
            )

            # If both lists have the same answer, add to same grouped list
            for q in revised_noun_list:
                revised_advanced_list += [q]
                revised_noun_list.remove(q)

            revised_advanced_list.append(sent)

            # Ensure first letter is capitalized
            revised_advanced_list = [
                str(q).replace(
                    str(q).split()[0],
                    str(q).split()[0].capitalize()
                ) for q in revised_advanced_list
            ]

            # Add to total list of questions
            if len(revised_advanced_list) > 1:
                printed = False
                for q in revised_advanced_list[:-1]:
                    if q in used_q:
                        revised_advanced_list.remove(q)

                if len(revised_advanced_list) > 1:
                    used_q += revised_advanced_list[:-1]
                    total_q_list += [revised_advanced_list]

        return (total_q_list, printed)


class RequestParser:
    def __init__(self, request):
        # For Unit Testing purposes
        try:
            self.request = request.POST
        except AttributeError:
            self.request = request

    # Print initial request without selections and parse
    def initial_question_request(self, input_):
        out = OpenFiles.open_output_file()

        qa_list_name = self.request.get('qatitle')

        total_q_list, printed = QuestionCreator(input_, ' ').final_q_list()

        Printer(out).initial_print(qa_list_name, input_)
        Printer(out).print_write(total_q_list)

        args = {
            'ogtext': input_,
            'questions': total_q_list,
            'range': range(1),
            'printed': printed
        }

        return args

    # Print initial request with selections and parse
    def selection_parsing(self):
        out = OpenFiles.open_output_file()

        selected_list = self.request.getlist('choices[]')
        input_ = self.request.get('og_input')
        qa_list_name = self.request.get('qatitle')

        try:
            total_q_list = (ast.literal_eval(self.request.getlist('og_list')[0]))

            final_list = []

            for ogq_list in total_q_list:
                for ogq in ogq_list[:-1]:
                    if ogq not in selected_list:
                        ogq_list.remove(ogq)

                if len(ogq_list) > 1:
                    final_list.append(ogq_list)

        except IndexError:
            final_list = (ast.literal_eval(self.request.getlist('choices[]')[0]))

        if 'createsession' not in self.request:
            Printer(out).initial_print(qa_list_name, input_)
            Printer(out).print_write(final_list)

        return (qa_list_name, final_list, input_)


class AnswerEvaluation:
    def __init__(self, userlist, actualist):
        self.userlist = userlist
        self.actualist = actualist

    def evaluate_similarity(self):
        total_sim = 0

        for usera, actuala in zip(self.userlist, self.actualist):
            user_answer_doc = ProcessInput("").get_nlp_doc(usera)
            actual_answer_doc = ProcessInput("").get_nlp_doc(actuala)
            total_sim += actual_answer_doc.similarity(user_answer_doc)

        return round((total_sim / len(self.userlist)) * 100, 1)


class Printer:
    def __init__(self, out):
        self.out = out

    def initial_print(self, title, og_input):
        writer_string = ''

        if title is not None:
            writer_string += (
                'Title: ' + str(title) + '\n\n'
            )

        writer_string += (
            '=================\n'
            '= Inputted Text =\n'
            '=================\n' +
            str(og_input) +
            '\n\n' + '*' * 100 + '\n\n'
        )

        self.out.write(writer_string)
        return 0

    def print_write(self, q_list):
        writer_string = ''
        num = 1

        for questions in q_list:
            if len(questions) > 1:
                answer = questions[-1]

                writer_string += (
                    '---------------\n'
                    '- Question(s) -\n'
                    '---------------\n'
                )

                for q in questions[:-1]:
                    writer_string += ('{}. {}\n'.format(num, q))
                    num += 1

                writer_string += '\n'

                writer_string += (
                    '----------\n'
                    '- Answer -\n'
                    '----------\n' + str(answer) + '\n\n'
                )

        self.out.write(writer_string)
        return 0
