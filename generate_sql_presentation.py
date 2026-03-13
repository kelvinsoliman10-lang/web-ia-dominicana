from fpdf import FPDF
from fpdf.enums import XPos, YPos

class SQLPresentation(FPDF):
    def __init__(self):
        super().__init__(orientation='landscape', unit='mm', format='A4')
        self.set_auto_page_break(auto=False)
        self.primary_blue = (10, 25, 47)
        self.accent_cyan = (100, 255, 218)
        self.text_grey = (204, 214, 246)
        self.white_color = (255, 255, 255)

    def header_slide(self, title, subtitle=None):
        self.add_page()
        # Background
        self.set_fill_color(r=10, g=25, b=47)
        self.rect(0, 0, 297, 210, 'F')
        
        # Design elements
        self.set_draw_color(r=100, g=255, b=218)
        self.set_line_width(0.5)
        self.line(20, 105, 277, 105)
        
        # Title
        self.set_font('helvetica', 'B', 48)
        self.set_text_color(r=255, g=255, b=255)
        self.set_y(70)
        self.cell(0, 20, title.encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        
        # Subtitle
        if subtitle:
            self.set_font('helvetica', 'I', 20)
            self.set_text_color(r=100, g=255, b=218)
            self.set_y(115)
            self.cell(0, 10, subtitle.encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def content_slide(self, title, content_list, code_snippet=None):
        self.add_page()
        # Background
        self.set_fill_color(r=10, g=25, b=47)
        self.rect(0, 0, 297, 210, 'F')
        
        # Sidebar/Top bar accent
        self.set_fill_color(r=100, g=255, b=218)
        self.rect(15, 15, 5, 20, 'F')
        
        # Title
        self.set_font('helvetica', 'B', 32)
        self.set_text_color(r=255, g=255, b=255)
        self.set_xy(30, 15)
        self.cell(0, 20, title.encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Content
        self.set_font('helvetica', '', 16)
        self.set_text_color(r=204, g=214, b=246)
        self.set_xy(30, 45)
        for item in content_list:
            safe_item = item.encode('latin-1', 'replace').decode('latin-1')
            self.multi_cell(0, 10, f"- {safe_item}", border=0, align='L')
            self.ln(2)
            
        # Code Snippet UI
        if code_snippet:
            self.set_fill_color(r=23, g=42, b=69)
            self.rect(30, self.get_y() + 5, 237, 40, 'F')
            self.set_xy(35, self.get_y() + 10)
            self.set_font('courier', 'B', 14)
            self.set_text_color(r=100, g=255, b=218)
            self.multi_cell(227, 8, code_snippet.encode('latin-1', 'replace').decode('latin-1'))

    def toc_slide(self, items):
        self.add_page()
        self.set_fill_color(r=10, g=25, b=47)
        self.rect(0, 0, 297, 210, 'F')
        
        self.set_font('helvetica', 'B', 32)
        self.set_text_color(r=255, g=255, b=255)
        self.set_xy(30, 15)
        self.cell(0, 20, "Indice de Contenidos".encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_font('helvetica', '', 14)
        self.set_text_color(r=204, g=214, b=246)
        self.set_xy(30, 45)
        
        col1 = items[:len(items)//2 + 1]
        col2 = items[len(items)//2 + 1:]
        
        y_start = 45
        for i, item in enumerate(col1):
            self.set_xy(30, y_start + (i*15))
            safe_item = item.encode('latin-1', 'replace').decode('latin-1')
            self.cell(100, 10, safe_item)
            
        for i, item in enumerate(col2):
            self.set_xy(160, y_start + (i*15))
            safe_item = item.encode('latin-1', 'replace').decode('latin-1')
            self.cell(100, 10, safe_item)

def generate():
    pdf = SQLPresentation()
    
    # 1. Portada
    pdf.header_slide("INTRODUCCION A SQL", "Dominando el Lenguaje de Datos")
    
    # 2. Indice
    toc_items = [
        "3.1 Introduccion",
        "3.2 Historia y estandarizacion",
        "3.3 Tipos de sentencias SQL",
        "3.4 Tipos de datos",
        "3.5 SQL*Plus",
        "3.6 iSQL*Plus",
        "3.7 Consulta de los datos",
        "3.8 Operadores aritmeticos",
        "Conclusion",
        "Referencias Bibliograficas"
    ]
    pdf.toc_slide(toc_items)
    
    # 3. Introducción
    pdf.content_slide("3.1 Introduccion", [
        "SQL (Structured Query Language) es el lenguaje estandar para bases de datos relacionales.",
        "Permite interactuar con Sistemas Gestores de Bases de Datos (RDBMS).",
        "Es un lenguaje declarativo: nos dice 'que' queremos, no 'como' obtenerlo.",
        "Crucial para analistas, desarrolladores y administradores de sistemas."
    ])
    
    # 4. Historia
    pdf.content_slide("3.2 Historia y estandarizacion", [
        "Creado por IBM en los anos 70 bajo el nombre SEQUEL.",
        "Relacionado directamente con el modelo relacional de Edgar F. Codd.",
        "ANSI e ISO establecieron estandares desde 1986 (SQL-86, SQL-92, etc.).",
        "Oracle fue de los primeros en comercializarlo con exito."
    ])
    
    # 5. Tipos de Sentencias
    pdf.content_slide("3.3 Tipos de sentencias SQL", [
        "DDL (Data Definition Language): Define la estructura (CREATE, ALTER, DROP).",
        "DML (Data Manipulation Language): Gestiona datos (SELECT, INSERT, UPDATE, DELETE).",
        "DCL (Data Control Language): Seguridad y permisos (GRANT, REVOKE).",
        "TCL (Transaction Control Language): Control de cambios (COMMIT, ROLLBACK)."
    ])
    
    # 6. Ejemplos de Sentencias
    pdf.content_slide("Ejemplos en Accion", [
        "Visualizacion rapida de sintaxis fundamental en SQL.",
        "Diferencia clara entre crear, insertar y consultar."
    ], code_snippet="CREATE TABLE usuarios (id NUMBER, nombre VARCHAR2(50));\nINSERT INTO usuarios VALUES (1, 'Admin');\nSELECT * FROM usuarios WHERE id = 1;")
    
    # 7. Tipos de Datos
    pdf.content_slide("3.4 Tipos de datos", [
        "VARCHAR2(n): Cadenas de caracteres de longitud variable.",
        "NUMBER(p, s): Valores numericos con precision y escala.",
        "DATE: Almacena fecha y hora con precision de segundos.",
        "CLOB / BLOB: Para grandes objetos de texto o binarios.",
        "ROWID: Identificador unico fisico de una fila."
    ])
    
    # 8. SQL*Plus
    pdf.content_slide("3.5 SQL*Plus", [
        "Herramienta interactiva de linea de comandos para bases de datos Oracle.",
        "Permite ejecutar sentencias SQL y comandos propios de administracion.",
        "Utilizado para automatizacion mediante scripts (.sql).",
        "Ligero, potente y disponible en todas las instalaciones de Oracle."
    ])
    
    # 9. iSQL*Plus
    pdf.content_slide("3.6 iSQL*Plus", [
        "Variante basada en interfaz web de SQL*Plus (clasica).",
        "Permite acceso remoto sin necesidad de cliente Oracle local profundo.",
        "Facilidad de visualizacion para resultados de consultas grandes.",
        "Reemplazado en versiones modernas por SQL Developer y APEX."
    ])
    
    # 10. Consulta de Datos
    pdf.content_slide("3.7 Consulta de los datos", [
        "La instruccion SELECT es el nucleo de SQL.",
        "Clausula FROM: Indica el origen de los datos (tablas/vistas).",
        "Clausula WHERE: Filtra filas basadas en condiciones especificas.",
        "Clausula ORDER BY: Ordena el resultado de forma ASC o DESC."
    ], code_snippet="SELECT nombre, salario FROM empleados \nWHERE departamento_id = 10 \nORDER BY salario DESC;")
    
    # 11. Operadores Aritméticos
    pdf.content_slide("3.8 Operadores aritmeticos", [
        "Suma (+), Resta (-), Multiplicacion (*) y Division (/).",
        "Se pueden usar en SELECT y WHERE para calculos al vuelo.",
        "Siguen reglas de precedencia matematica estandar.",
        "Uso de alias (AS) para nombrar columnas calculadas."
    ], code_snippet="SELECT nombre, salario, (salario * 1.1) AS salario_bonus \nFROM empleados;")
    
    # 12. Conclusión y Referencias
    pdf.content_slide("Conclusion y Referencias", [
        "SQL is the piedra angular del manejo de datos masivos.",
        "Dominar SQL*Plus es esencial para entornos corporativos Oracle.",
        "Referencias: \n- Oracle Database Documentation Library.\n- ANSI/ISO Framework (ISO/IEC 9075).\n- 'Sistemas de Bases de Datos' de Silberschatz et al."
    ])
    
    output_path = "Introduccion_a_SQL.pdf"
    pdf.output(output_path)
    print(f"PDF generado exitosamente en: {output_path}")

if __name__ == "__main__":
    generate()
