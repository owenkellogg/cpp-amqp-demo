from conans import ConanFile, CMake

class CPPAappTemplateConan(ConanFile):
    name = "CppAppTemplate"
    version = "0.2.4"
    license = "OpenSource"
    author = "Powco"
    url = "https://github.com/ProofOfWorkCompany/cpp-app-template"
    description = "Best practices with c++"
    topics = ("what", "this", "app", "is", "about")
    settings = "os", "compiler", "build_type", "arch"   
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "src/*"
    requires = ["argh/1.3.2", "gtest/1.12.1", "websocketpp/0.8.2", "boost/1.81.0"]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("CPPAappTemplate", dst="bin", keep_path=False)
