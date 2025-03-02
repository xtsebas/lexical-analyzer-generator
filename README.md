# Lexical Analyzer Generator

Este proyecto es un **generador de analizadores léxicos** en Python, basado en la especificación de tokens escrita en **YALex**. 

## 📌 Características
- **Genera un analizador léxico en Python** a partir de un archivo `.yal`.
- **Dibuja el diagrama de transición de estados** basado en la definición del autómata.
- **Detecta tokens y errores léxicos** en archivos de entrada de diferentes niveles de complejidad.
- **Incluye una interfaz gráfica** para facilitar su uso.

---

## 📁 Estructura del Proyecto
```bash
LEXICAL-ANALYZER-GENERATOR
│── examples/                 # Archivos de prueba con diferentes niveles de complejidad
│   ├── simple.yal
│   ├── medium.yal
│   ├── complex.yal
│   ├── input_low.txt
│   ├── input_medium.txt
│   ├── input_complex.txt
│
│── gui/                      # Interfaz gráfica
│   ├── main.py               # Script principal de la GUI
│
│── output/                   # Archivos generados automáticamente
│   ├── generated_lexer.py    # Código del analizador léxico generado
│
│── src/                      # Código fuente principal
│   ├── generator.py          # Código principal del generador
│   ├── lexer_template.py     # Plantilla base para el analizador generado
│   ├── regex_parse.py        # Módulo que interpreta expresiones regulares
│   ├── state_diagram.py      # Generación del diagrama de estados
│   ├── utils.py              # Funciones auxiliares
│
│── test/                     # Pruebas automatizadas
│   ├── test_generator.py     # Pruebas para el generador
│
│── .gitignore                # Archivos a ignorar en el repositorio
│── requirements.txt          # Dependencias necesarias
```

---

## 🚀 Instalación y Ejecución

### 🔹 Requisitos previos
Asegúrate de tener **Python 3.x** instalado en tu sistema. Luego, instala las dependencias:
```sh
pip install -r requirements.txt
```

### 🔹 Generar un Analizador Léxico
Para generar un analizador léxico a partir de un archivo `.yal`, usa:
```sh
python src/generator.py examples/simple.yal
```
Esto generará el archivo `generated_lexer.py` en la carpeta `output/`.

### 🔹 Ejecutar el Analizador Léxico
Una vez generado el analizador, puedes ejecutarlo con un archivo de entrada:
```sh
python output/generated_lexer.py examples/input_low.txt
```

### 🔹 Ejecutar la Interfaz Gráfica
Si prefieres usar la interfaz gráfica, ejecuta:
```sh
python gui/main.py
```

---

## 📌 Ejemplo de Código en YALex
Un ejemplo simple de archivo en **YALex** que reconoce operadores matemáticos y números enteros:
```yalex
rule gettoken =
    [' ' '\t'] { return lexbuf } (* Ignorar espacios *)
  | ['\n' ] { return EOL }  (* Salto de línea *)
  | ['0'-'9']+ { return int(lxm) } (* Números *)
  | '+' { return PLUS }
  | '-' { return MINUS }
```
  | '*' { return TIMES }
  | '/' { return DIV }
  | '(' { return LPAREN }
  | ')' { return RPAREN }
  | eof { raise('Fin de buffer') }
\`\`\`
