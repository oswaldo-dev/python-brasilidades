from cpf_cnpj import Documento

# cpf = Cpf("012.345.678-90")
# print(cpf)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "48812321003"
documento = Documento.cria_documento(exemplo_cnpj)
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento)
print(documento2)