from fpdf import FPDF
import os

# Carpeta donde se guardarán los PDFs generados
PDF_FOLDER = 'generated_pdfs'
os.makedirs(PDF_FOLDER, exist_ok=True)

def generar_pdf(cliente, proyecto, celular, correo_asesor, correo, ubicacion, 
                potencia, costo, area, consumo_anual, paneles_400, paneles_585, paneles_605):
    """Genera un archivo PDF con la cotización del proyecto solar."""

    # Crear el PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    # Logo centrado
    logo_path = "./static/css/imagenes/logo_ferragro.png"
    logo_width = 50  # Ancho del logo
    logo_height = 20  # Ajusta según el tamaño real del logo
    pdf.image(logo_path, x=(210 - logo_width) / 2, y=10, w=logo_width)  # Centrado dinámico

    # Ajustar espacio después del logo
    pdf.ln(logo_height + 10)  # Asegura suficiente espacio antes del título

    # Título
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Cotización de Proyecto Solar", ln=True, align='C')
    pdf.ln(10)
    
    # Información del cliente
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Proyecto: {proyecto}", ln=True)
    pdf.cell(200, 10, txt=f"Correo: {correo}", ln=True)
    pdf.cell(200, 10, txt=f"celular: {celular}", ln=True)
    pdf.cell(200, 10, txt=f"Correo del asesor: {correo_asesor}", ln=True)
    pdf.cell(200, 10, txt=f"Zona del proyecto: {ubicacion}", ln=True)
    pdf.cell(200, 10, txt=f"Potencia Instalada: {potencia} kWp", ln=True)
    pdf.cell(200, 10, txt=f"Área Disponible: {area} m²", ln=True)
    pdf.cell(200, 10, txt=f"Costo del kWp mensual: ${costo}", ln=True)
    
    pdf.ln(10)  # Espacio

    #PANELES SOLARES
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(200, 10, txt="Cálculo de Consumo y Paneles", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt=f"Consumo Anual Estimado: {consumo_anual} kWh", ln=True)
    pdf.cell(200, 10, txt=f"Número de Paneles de 400W: {paneles_400}", ln=True)
    pdf.cell(200, 10, txt=f"Número de Paneles de 585W: {paneles_585}", ln=True)
    pdf.cell(200, 10, txt=f"Número de Paneles de 605W: {paneles_605}", ln=True)

    # Guardar el PDF
    pdf_path = os.path.join(PDF_FOLDER, 'cotizacion.pdf')
    pdf.output(pdf_path)

    return pdf_path