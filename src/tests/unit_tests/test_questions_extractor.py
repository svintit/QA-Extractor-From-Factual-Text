import pickle
from ...extractor_libs import question_extractor as QE

# Preprocessing needs to be done to retrieve correct inputs.

with open('src/tests/unit_tests/request.pickle', 'rb') as pk:
    request_ = pickle.load(pk)


test_input = (
    'This is a test.'
    'Monrovia was named after James Monroe.'
    'Passing this test is easy.'
)

test_out = QE.OpenFiles.open_output_file()
test_process_input = QE.ProcessInput(test_input)
sentences = test_process_input.tok_sent()

test_total_sent = []
test_doc = []
test_pos_tagged = []
test_noun_chunks = []

test_advanced_q_list = []
test_n_chunk_q_list = []
test_merged_lists = []
test_q_decider_list = []

for test_sent in sentences:
    doc = test_process_input.get_nlp_doc(test_sent)

    # Test_ProcessInput
    test_total_sent.append(str(test_sent))
    test_doc.append(str(test_process_input.get_nlp_doc(str(test_sent))))
    test_pos_tagged += [test_process_input.pos_tag(doc)]
    test_noun_chunks.append(test_process_input.n_chunk(doc))

    # Test_QuestionCreator
    test_question_creator = QE.QuestionCreator(doc, test_sent)

    pos_tagged = test_process_input.pos_tag(doc)
    test_advanced_q_list.append(
        test_question_creator.advanced_q(pos_tagged)
    )

    noun_chunks = test_process_input.n_chunk(doc)
    test_n_chunk_q_list.append(
        test_question_creator.n_chunk_q(noun_chunks, 2)
    )

    test_decided_list = test_question_creator.q_decider(
        test_n_chunk_q_list, 1
    )

    test_merged_lists += [test_advanced_q_list]
    test_merged_lists += [test_n_chunk_q_list]


class Test_OpenFiles:
    def test_open_output_file_return_None(self):
        assert str(type(test_out)) == "<class '_io.TextIOWrapper'>"


class Test_ProcessInput(object):
    def test_tok_sent_return_tokenized(self):
        assert test_total_sent == [
            'This is a test.',
            'Monrovia was named after James Monroe.',
            'Passing this test is easy.'
        ]

    def test_get_nlp_doc_return_spacy_tok(self):
        assert test_doc == [
            'This is a test.',
            'Monrovia was named after James Monroe.',
            'Passing this test is easy.'
        ]

    def test_pos_tag_return_list(self):
        assert test_pos_tagged == [
            [
                ['This', 'DET'],
                ['is', 'VERB'],
                ['a', 'DET'],
                ['test', 'NOUN'],
                ['.', 'PUNCT']
            ],
            [
                ['Monrovia', 'PROPN'],
                ['was', 'VERB'],
                ['named', 'VERB'],
                ['after', 'ADP'],
                ['James', 'PROPN'],
                ['Monroe', 'PROPN'],
                ['.', 'PUNCT']
            ],
            [
                ['Passing', 'VERB'],
                ['this', 'DET'],
                ['test', 'NOUN'],
                ['is', 'VERB'],
                ['easy', 'ADJ'],
                ['.', 'PUNCT']
            ]
        ]

    def test_n_chunk_return_list(self):
        assert test_noun_chunks == [
            [
                ['a test', 'is']
            ],
            [
                ['Monrovia', 'named'],
                ['James Monroe', 'after']
            ],
            [
                ['this test', 'Passing']
            ]
        ]


class Test_QuestionCreator(object):
    def test_advanced_q_return_list(self):
        assert test_advanced_q_list == [
            [],
            [
                'what was named after James Monroe?',
                'In the context of this text, '
                'what was named after James Monroe?',
                'As given in the text, what was named after James Monroe?',
                'what was named after James Monroe, as stated in the text?'
            ],
            []
        ]

    def test_n_chunk_q_return_list(self):
        assert test_n_chunk_q_list == [
            [],
            [
                'Why was Monrovia mentioned?',
                'Who is James Monroe in the context of this text?'
            ],
            []
        ] or [
            [],
            [
                'Why was Monrovia mentioned?',
                'Why is James Monroe mentioned?'
            ],
            []
        ]

    def test_q_decider_return_list(self):
        assert str(type(test_decided_list)) == "<class 'list'>"

    def test_final_q_list(self):
        assert str(type(QE.QuestionCreator(
            test_input, ' '
        ).final_q_list())) == "<class 'tuple'>"


class Test_RequestParser(object):
    def test_initial_question_request_return_dict(self):
        test_initial_request = QE.RequestParser(request_).initial_question_request(test_input)
        assert str(type(test_initial_request)) == "<class 'dict'>"

    def test_selection_parsing_return_tup(self):
        test_list_name, test_final_list, input_ = QE.RequestParser(request_).selection_parsing()
        types = str(type(test_list_name)) + str(type(test_final_list)) + str(type(input_))
        assert types == "<class 'str'><class 'list'><class 'str'>"


class Test_AnswerEvaluation(object):
    def test_evaluate_similarity_return_int(self):
        actualanswer = ["James Monroe was the president of the United States in 1822."]
        useranswer = ["James Monroe was the president of the United States in 1822."]
        assert QE.AnswerEvaluation(useranswer, actualanswer).evaluate_similarity() == 100


class Test_Printer(object):
    def test_initial_print_return_0(self):
        test_initial_print = QE.Printer(test_out).initial_print("", test_input)
        assert test_initial_print == 0

    def test_print_write_return_0(self):
        test_print_write = QE.Printer(test_out).print_write(test_merged_lists)
        assert test_print_write == 0
