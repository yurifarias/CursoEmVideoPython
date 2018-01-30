tipoPrimitivo = input('Digite algo: ')

print('O tipo primitivo é do tipo:', type(tipoPrimitivo))

print('O que você digitou é número?', tipoPrimitivo.isnumeric())
print('O que você digitou é texto?', tipoPrimitivo.isalpha())
print('O que você digitou é espaço?', tipoPrimitivo.isspace())
print('O que você digitou é alfanumérico?', tipoPrimitivo.isalnum())
