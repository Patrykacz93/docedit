from docxtpl import DocxTemplate


class Generate:

    def __init__(self):
        self.dokument = DocxTemplate('RETURN AUTHORIZATION FORM_2.0.docx')
        self.context = {'rma': 'RMA/2022/01/01',
                        'cp': 'BTiB',
                        'mail': 'elo@gmail.com',
                        'csd': 'CSD-300',
                        'date': '10.10.2022',
                        'device': 'AAC20',
                        'sn': '233445',
                        'fw': '2.1',
                        'problem': 'rozjebalo sie'}

        self.nowydoc = self.dokument.render(self.context)
        self.dokument.save('newRETURN AUTHORIZATION FORM_2.0.docx')

