#Keras implementation of Deeplabv3+
#pip3 install pyenchant
#us US vocabulary for NLP analysis

import enchant
d = enchant.Dict("en_US") # dictionary 
d.check("Hello")
d.check("Helo")
d.check("Hlo")
#get firts on on the list as the closest suggested word
d.suggest("aricle")
