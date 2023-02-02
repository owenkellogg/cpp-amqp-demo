cmake_minimum_required(VERSION 3.16)
project(CppAppTemplate CXX)

# Setup paths to outputs of conan's "cmake_find_package" generator
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(libCPPTemplate STATIC
    src/logger.cpp)
    
target_include_directories(libCPPTemplate PUBLIC include)
target_compile_features(libCPPTemplate PUBLIC cxx_std_20)
set_target_properties(libCPPTemplate PROPERTIES CXX_EXTENSIONS OFF)

add_executable(CppAppTemplate src/main.cpp)

target_link_libraries(CppAppTemplate PUBLIC
  libCPPTemplate
  CONAN_PKG::argh
  CONAN_PKG::websocketpp
  CONAN_PKG::boost
)

target_include_directories(CppAppTemplate PUBLIC include)
target_compile_features(CppAppTemplate PUBLIC cxx_std_20)
set_target_properties(CppAppTemplate PROPERTIES CXX_EXTENSIONS OFF)

add_executable(Websockets src/websockets.cpp)

target_link_libraries(Websockets PUBLIC
  libCPPTemplate
  CONAN_PKG::argh
  CONAN_PKG::boost
)

target_include_directories(Websockets PUBLIC include)
target_compile_features(Websockets PUBLIC cxx_std_20)
set_target_properties(Websockets PROPERTIES CXX_EXTENSIONS OFF)

option(PACKAGE_TESTS "Build the tests" ON)

#uncomment this if you are using cpp boost libraries
#add_definitions("-DHAS_BOOST")

if(PACKAGE_TESTS)
  include(CTest)
  find_package(GTest REQUIRED)
  enable_testing()
  add_subdirectory(test)

endif()
