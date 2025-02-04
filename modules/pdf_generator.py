from fpdf import FPDF
import os

# Carpeta donde se guardarán los PDFs generados
PDF_FOLDER = 'generated_pdfs'
os.makedirs(PDF_FOLDER, exist_ok=True)

def generar_pdf(cotizacion, fecha, cliente, proyecto, celular, correo_asesor ,correo , ubicacion, potencia, costo, area, datos_proyecto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)  # Auto ajuste del contenido
    
    pdf.set_font('Arial', size=12)
    
    # LOGO CENTRADO
    logo_path = "./static/css/imagenes/logo solartech.png"
    logo_width = 100  
    pdf.image(logo_path, x=(pdf.w - logo_width) / 2, y=10, w=logo_width)

    pdf.ln(30)

    # TITULO Y FECHA
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, txt=f"Cotización #{cotizacion}", ln=True, align='C')
    pdf.cell(0, 10, txt="Cotización de Proyecto de Energía Solar", ln=True, align='C')
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 10, txt=f"Fecha: {fecha}", ln=True, align='C') 
    pdf.ln(10)
    
    #IMAGEN
    imagen_path = "./static/css/imagenes/NATURAL_HARVEST.jpeg"
    image_width = 200
    image_height = 80
    pdf.image(imagen_path, x=(pdf.w - image_width) / 2, w=image_width, h=image_height)
    pdf.ln(10)
    
    # ✅ **TABLA DE INFORMACIÓN DEL CLIENTE**
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, txt="Datos proporcionados por el Cliente", ln=True, align='C')
    pdf.ln(5)

    # Ajustar ancho de columnas
    col_width = (pdf.w - 20) / 2  

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(col_width, 8, txt="Campo", border=1, align='C')
    pdf.cell(col_width, 8, txt="Valor", border=1, align='C')
    pdf.ln()

    pdf.set_font('Arial', size=12)
    cliente_info = [
        ("Cliente", cliente),
        ("Correo", correo),
        ("Proyecto", proyecto),
        ("Celular", celular),
        ("Correo Asesor", correo_asesor),
        ("Ubicación", ubicacion),
        ("Potencia", f"{potencia} kWp"),
        ("Costo del kWp", f"${costo}"),
        ("Área Disponible", f"{area} m²")
    ]

    for campo, valor in cliente_info:
        pdf.cell(col_width, 8, txt=campo, border=1)
        pdf.cell(col_width, 8, txt=str(valor), border=1, align='C')
        pdf.ln()

    pdf.ln(10)

    # ✅ **TABLA DE RESULTADOS DEL PROYECTO**
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, txt="Resultados del Proyecto", ln=True, align='C')
    pdf.ln(5)

    pdf.set_font('Arial', 'B', 12)
    col_width = (pdf.w - 20) / 2
    pdf.cell(col_width, 8, txt="Concepto", border=1, align='C')
    pdf.cell(col_width, 8, txt="Valor", border=1, align='C')
    pdf.ln()

    pdf.set_font('Arial', size=12)

    # Unidades de medida según concepto
    unidades = {
        "Consumo Anual (kWh)": "kWh",
        "Energía generada por panel de 400W": "kWh",
        "Energía generada por panel de 585W": "kWh",
        "Energía generada por panel de 605W": "kWh",
        "Número de paneles de 400W": "unidades",
        "Número de paneles de 585W": "unidades",
        "Número de paneles de 605W": "unidades",
        "Número de inversores de 3500W": "(unidades)",
        "Número de inversores de 6000W": "(unidades)",
        "Número de inversores de 6000W": "(unidades)",
        "Número de inversores de 6000W": "(unidades)",
        # Baterias gel
        "Número de Baterías Gel 100Ah": "(unidades)",
        "Número de Baterías Gel 150Ah": "(unidades)",
        "Número de Baterías Gel 200Ah": "(unidades)",
        "Número de Baterías Gel 250Ah": "(unidades)",
        # Baterias Litio
        "Número de Baterías litio 60Ah": "(unidades)",
        "Número de Baterías litio 100Ah": "(unidades)",
        "Número de Baterías litio 120Ah": "(unidades)",
        "Número de Baterías litio 150Ah": "(unidades)",
        "Número de Baterías litio 2000Ah": "(unidades)",
        # Estructura
        "Número de Rieles 4.7m 400W": "(unidades)",
        "Número de Midcland 400W": "(unidades)",
        "Número de Endcland 400W": "(unidades)"
    }
    

    for key, value in datos_proyecto.items():
        pdf.cell(col_width, 8, txt=key, border=1)
        
        # Verifica si es un número y lo formatea con separador de miles
        if isinstance(value, (int, float)):
            formatted_value = "{:,.2f}".format(value).replace(",", ".")
            unit = unidades.get(key, "")  # Obtiene la unidad si existe
            value_str = f"{formatted_value} {unit}".strip()
        else:
            value_str = str(value)  # Si no es número, lo deja como está

        pdf.cell(col_width, 8, txt=value_str, border=1, align='C')
        pdf.ln()

    # ✅ **CONDICIONES DEL PROYECTO**
    condiciones_path = "modules/condiciones.txt"
    if os.path.exists(condiciones_path):
        with open(condiciones_path, "r", encoding="utf-8") as file:
            condiciones = file.read()

        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, txt="Condiciones del Proyecto", ln=True, align='C')
        pdf.ln(5)
        
        pdf.set_font('Arial', size=10)
        pdf.multi_cell(0, 8, condiciones, border=1, align='J')

    pdf_path = os.path.join(PDF_FOLDER, f'cotizacion_{cotizacion}.pdf')
    pdf.output(pdf_path)

    return pdf_path
