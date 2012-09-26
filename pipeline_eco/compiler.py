from pipeline.compilers import CompilerBase
from django.core.files.base import ContentFile
from django.utils.encoding import smart_str

import os
import eco

class EcoCompiler(CompilerBase):
    output_extension = 'js'

    def match_file(self, filename, **kwargs):
        return filename.endswith('.eco')

    def compile_file(self, content, path, force=False, outdated=False, **kwargs):
        if force or outdated:
            str_ = u'(function() {{\n  this.JST || (this.JST = {{}});\n  this.JST["{0}"] = {1};\n \n}}).call(this);'
            compiled_content = str_.format(self._template_name(content), eco.compile(open(content)))
            self.save_file(path, compiled_content)

    def _template_name(self, infile):
        p = infile.split("/")[::-1]
        return os.path.join(p[1], p[0].split(".")[0])

    def save_file(self, path, content):
        return open(path, 'w').write(smart_str(content))