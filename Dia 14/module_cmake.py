# MODULO CMAKE
# El módulo se puede utillizar para generar archivos de construcción CMake, configurar proyectos CMake y construir proyectos CMake.

# Metodos
    # add_executable(MyApp main.cpp helper.cpp): crear un ejecutable CMake
    # add_library(MyLibrary library.cpp): crea una biblioteca CMake
    # add_subdirectoru(MY_VARIABLE "some_value"): agrega un subdirectorio CMake
    # configure(): configura un proyecto CMake
    # build(): construye un proyecto CMake
# Atributos
    # CMAKE_C_COMPILER: el compilador C de CMake
    # CMAKE_CXX_COMPILER: el compilador C++ de CMake
    # CMAKE_BUILD_TYPE: el tipo de construcción de CMake
    # CMAKE_INSTALL_PREFIX: la ruta de instalación de CMake
# Parametros
    # CMAKE_MODULE_PATH: la ruta al directorio que contiene los módulos CMake
    # CMAKE_PREFIX_PATH: la ruta al directorio que contiene las bibliotecas CMake
    # CMAKE_SYSTEM_NAME: el nombre del sistema operativo de destino
    # CMAKE_SYSTEM_PROCESSOR: el procesador de destino

'EJEMPLO'

import cmake

# Crea un ejecutable CMake
cmake.add_executable('hello', 'hello.c')

# Configura el proyecto CMake
cmake.configure()

# Construye el proyecto CMake
cmake.build()
