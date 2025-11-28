"""
3rd layer of obfuscation
"""
import random,string
import base64,lzma,zlib
import marshal,py_compile

class Layer3:
    def __init__(self, code, symbol, file):
        self.code = code
        self.chars = string.ascii_letters
        self.symbol = symbol
        self.file = file

    def vars(self):
        rndint = random.randint(10,50)
        random_vars = ''.join(random.choice(self.chars) for i in range(rndint))
        return random_vars
    
    def zip(self, cd):
        xx = lzma.compress(cd.encode())
        return xx

    def encrypt_low_level(self):
        code = self.code
        encrypted = ""
        encrypted2 = ""
    
        junky = f'{self.vars()*random.randint(1,10)}="{self.vars()*random.randint(1,20)}";'
        zero = f'{self.vars()}="invalid code lol xD"'
        cc = compile(zero, self.symbol, "exec")
        cc = marshal.dumps(cc)
        cc = repr(cc)
        cc = f'exec(marshal.loads({cc}))'
        cc = base64.b64encode(cc.encode())
        junks = f'{self.symbol}=exec(base64.b64decode({cc}));'
        cc1 = self.zip(junks)
        cc2 = f'exec(lzma.decompress({cc1}));'
        maxjunk = f'{junky}{cc2}'
        encrypted += maxjunk  

        abc = compile(code, self.symbol, "exec")
        abcd = marshal.dumps(abc)
        abcde = repr(abcd)
        run = f'exec(marshal.loads({abcde}));'
        runq = base64.b64encode(run.encode())
        runa = f'{self.symbol}=exec(base64.b64decode({runq}));'
        cc3 = self.zip(runa)
        cc4 = f'exec(lzma.decompress({cc3}));'
        rrna = f'{self.vars()*random.randint(1,10)}="{self.vars()*random.randint(1,20)}";{cc4}'
        encrypted2 += encrypted
        encrypted2 += rrna
        encrypted2 += encrypted

        return encrypted2
    def encrypt_high_level(self):
        ok = self.zip(self.encrypt_low_level())
        oke = f'exec(lzma.decompress({ok}))'
        okk = self.zip(oke)
        okke = f'exec(lzma.decompress({okk}))'
        
        return okke

    def layer3_done(self):
        final_code = self.encrypt_high_level()
        new_name = self.file+"-obf.py"
        with open("./output/"+new_name, 'w') as output:
            output.write(f'# -- PYSHIELD Obfuscator -- :\n\nimport base64,marshal,lzma\n{final_code}')
        

    