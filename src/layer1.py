"""
First Layer of obfuscation : changing variable names , functions...
this one makes code looks complicated and hard to read
"""
import io
import os
import re
import ast
import tokenize
import astor
import random

class Layer1:
    def __init__(self, source):
        self.source = source

    def rename(self):
        code = self.remove_docs()
        parsed = ast.parse(code)
        
        funcs = {
            x for x in ast.walk(parsed) if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef))
        }

        classes = {
            x for x in ast.walk(parsed) if isinstance(x, ast.ClassDef)
        }

        args = {
            x.id for x in ast.walk(parsed) if isinstance(x, ast.Name) and not isinstance(x.ctx, ast.Load)
        }

        attrs = {
            x.attr for x in ast.walk(parsed) if isinstance(x, ast.Attribute) and not isinstance(x.ctx , ast.Load)
        }

        for func in funcs:
            if func.args.args:
                for arg in func.args.args:
                    args.add(arg.arg)
            if func.args.kwonlyargs:
                for arg in func.args.kwonlyargs:
                    args.add(arg.arg)
            if func.args.vararg:
                args.add(func.args.vararg.arg)
            if func.args.kwarg:
                args.add(func.args.kwarg.arg)

        def generate_obfuscated_name():
            patterns = [
                lambda: random.choice([''+'_'])+'O0' * random.randint(6, 12),
                lambda: 'I1l' * random.randint(4, 8),
                lambda: '_'+'O'.join(random.choices('O0Il1', k=random.randint(10, 20))),
                lambda: '_'+'Xx' * random.randint(3, 7) + '0' * random.randint(2, 5),
            ]
            return random.choice(patterns)()

        pairs = {}
        used = set()

        all_items = []
        for func in funcs:
            if func.name != "__init__":
                all_items.append(('func', func.name))
        for _class in classes:
            all_items.append(('class', _class.name))
        for arg in args:
            all_items.append(('arg', arg))
        for attr in attrs:
            all_items.append(('attr', attr))

        random.shuffle(all_items)

        for item_type, name in all_items:
            newname = generate_obfuscated_name()
            while newname in used:
                newname = generate_obfuscated_name()
            used.add(newname)
            pairs[name] = newname

        string_regex = r"('|\")[\x1f-\x7e]{1,}?('|\")"
        original_strings = re.finditer(string_regex, code, re.MULTILINE)
        originals = []

        for matchNum, match in enumerate(original_strings, start=1):
            originals.append(match.group().replace("\\", "\\\\"))

        placeholder = os.urandom(16).hex()
        code = re.sub(string_regex, f"'{placeholder}'", code, 0, re.MULTILINE)

        for i in range(len(originals)):
            for key in pairs:
                originals[i] = re.sub(r"\b" + re.escape(key) + r"\b", pairs[key], originals[i])

        max_iterations = 5
        for iteration in range(max_iterations):
            code_before = code
            code = self.do_rename(pairs, code)
            if code == code_before:
                break

        
        replace_placeholder = r"('|\")" + placeholder + r"('|\")"
        for original in originals:
            code = re.sub(replace_placeholder, original, code, 1, re.MULTILINE)

        return code
    def do_rename(self, pairs, code):
        for key in pairs:
            code = re.sub(r"\b" + re.escape(key) + r"\b", pairs[key], code)
        return code
    
    def remove_docs(self):
        parsed_s = ast.parse(self.source)

        class StringRemover(ast.NodeTransformer):
            def visit_Expr(self, node):
                if isinstance(node.value, ast.Str):
                    return None
                return node
        
        modified_ast = StringRemover().visit(parsed_s)
        
        if hasattr(ast, 'unparse'):
            return ast.unparse(modified_ast)
        else:
            return astor.to_source(modified_ast)
    
    def layer1_done(self):
        return (self.rename())
    
    