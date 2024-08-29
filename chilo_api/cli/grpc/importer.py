import importlib
import os


class GRPCImporter:

    def get_imported_modules(self, file_list):
        modules = []
        for file_path in file_list:
            module = self.get_imported_module(file_path)
            modules.append(module)
        return modules
            
    def get_imported_module(self, file_path):
        import_path = file_path.replace(os.sep, '.')
        spec = importlib.util.spec_from_file_location(import_path, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
