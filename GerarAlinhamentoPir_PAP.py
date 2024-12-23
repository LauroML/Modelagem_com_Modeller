# Importando o modeller
from modeller import *
from modeller.automodel import *

# Novo ambiente para o modeller
env = environ()

# Novo ambiente para o alinhamento
aln = alignment(env)

# Modelo alvo. File= ID do PDB molde.
# Model_segment= Cadeia usada do molde
md1 = model(env, file='6u9w', model_segment=('FIRST:A', 'LAST:C'))

# Alinhamento. 
# Align_codes= PDB do molde e cadeia. 
# Atom_files= Nome do arquivo PDB do molde
aln.append_model(md1, align_codes='6u9w', atom_files='6u9w.pdb')

# Fazer o alinhamento. 
# File= arquivo com sequência do alvo. 
# Align_codes= ID do alvo.
aln.append(file='Q64663pir.txt', align_codes='RAttusP2X7')

# Alinhamento de sequências
aln.align2d(max_gap_length=50, fit=True)

# Arquivos de alinhamento formato PIR
aln.write(file='RAttusP2X7.ali', alignment_format='PIR')

# Arquivos de alinhamento formato PAP
aln.write(file='RAttusP2X7.pap', alignment_format='PAP')
