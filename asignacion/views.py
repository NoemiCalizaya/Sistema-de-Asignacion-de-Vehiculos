from django.shortcuts import redirect
from django.core import serializers
from django.core.serializers import serialize
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

# Create your views here.
class InicioAsignacion(TemplateView):
    template_name = 'asignacion/listaAsignaciones.html'

class RegistrarAsignacion(CreateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/crearAsignacion.html'
    success_url = reverse_lazy('index-asignacion')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio-asignacion')

class ListadoAsignacion(ListView):
    model = Asignacion_Vehiculo
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('inicio-asignacion')

class AsignacionDetailView(DetailView):
    model = Asignacion_Vehiculo
    template_name = 'asignacion/detalleAsignacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asignacion = self.model.objects.get(id = self.kwargs['pk'], estado = True)
        if asignacion.verificacion_entrega:
            asignacion.verificacion_entrega = "Realizado"
        else:
            asignacion.verificacion_entrega = "No Realizado"
        
        if asignacion.entrega:
            asignacion.entrega = "Realizado"
        else:
            asignacion.entrega = "No Realizado"
        
        if asignacion.verificacion_devolucion:
            asignacion.verificacion_devolucion = "Realizado"
        else:
            asignacion.verificacion_devolucion = "No Realizado"

        if asignacion.devolucion:
            asignacion.devolucion = "Realizado"
        else:
            asignacion.devolucion = "No Realizado"
        
        if asignacion.fecha_devolucion is None:
            asignacion.fecha_devolucion = " "
        
        context['asignacion'] = asignacion
        return context

class EditarAsignacion(UpdateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/editarAsignacion.html'
    success_url = reverse_lazy('index-asignacion')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio-asignacion')

class EditarDevolucion(UpdateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/editarDevolucion.html'
    success_url = reverse_lazy('index-asignacion')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            print(form)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio-asignacion')

class EliminarAsignacion(DeleteView):
    model = Asignacion_Vehiculo
    template_name = 'asignacion/eliminarAsignacion.html'

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            asignacion = self.get_object()
            asignacion.estado = False
            asignacion.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('inicio-asignacion')

from django.views import View
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.pagesizes import letter, landscape, inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Frame, PageTemplate
from reportlab.lib.utils import ImageReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter,A4,portrait
from reportlab.platypus import Image

class ReporteAsignacionVehiculo(View):
    def border(self,pdf):
        pdf.roundRect(20,196,752,390,4,stroke=1, fill=0)
        pdf.roundRect(16,190,760,400,4,stroke=1, fill=0)

    def header(self, pdf, asignacion):
        archivo_imagen = settings.MEDIA_ROOT+'/images/logo.png'
        imagen_auto = settings.MEDIA_ROOT+'/images/autopdf.png'
        imagen_escudob = settings.MEDIA_ROOT+'/images/escudo_boliviajpg.jpg'
        pdf.drawImage(imagen_escudob, 30, 505, 110, 80,preserveAspectRatio=True)  
        pdf.setFont("Helvetica", 10)
        pdf.drawString(170, 560, u"GOBIERNO AUTÓNOMO DEPARTAMENTAL DE POTOSÍ")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(145, 540, u"SECRETARÍA DEPARTAMENTAL ADMINISTRATIVA Y FINANCIERA")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(178, 520, u"ACTIVOS FIJOS - BIENES INMUEBLES Y SERVICIOS")
        pdf.setFont("Helvetica", 14)
        if asignacion.verificacion_devolucion == False:
            pdf.drawString(300, 480, u"ASIGNACIÓN DE VEHÍCULO")
        else:
            pdf.drawString(300, 480, u"DEVOLUCIÓN DE VEHÍCULO")
        pdf.drawImage(archivo_imagen, 650, 495, 110, 80,preserveAspectRatio=True)
        pdf.drawImage(imagen_auto, 540, 446, 110, 80,preserveAspectRatio=True)
        self.border(pdf)

    def tabla(self,pdf,y,asignacion, vehiculo):

        imagen_bien = settings.MEDIA_ROOT+'/images/bien.png'
        image = Image(imagen_bien, width=1.5 * inch, height=1.5 * inch)

        style = ParagraphStyle(name='Normal')
        text = 'VERIFICACIÓN ENTREGA'
        line11 = Paragraph(text, style)
        if asignacion.verificacion_entrega == True:
            line12 = image
            line12.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line12.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line12.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line12 = Paragraph(' ', style)
        text = 'ENTREGA'
        line13 = Paragraph(text, style)
        if asignacion.entrega == True:
            line14 = image
            line14.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line14.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line14.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line14 = Paragraph(' ', style)
        text = 'FECHA DE ASIGNACIÓN: '+str(asignacion.fecha)
        line15 = Paragraph(text, style)
        text = 'ID. SENAPE: '+str(asignacion.id_senape)
        line16 = Paragraph(text, style)
        text = 'VERIFICACIÓN DEVOLUCIÓN'
        line21 = Paragraph(text, style)
        if asignacion.verificacion_devolucion == True:
            line22 = image
            line22.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line22.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line22.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line22 = Paragraph(' ', style)
        text = 'DEVOLUCIÓN'
        line23 = Paragraph(text, style)
        if asignacion.devolucion == True:
            line24 = image
            line24.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line24.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line24.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line24 = Paragraph(' ', style)
        text = 'FECHA DE DEVOLUCIÓN: '+str(asignacion.fecha_devolucion)
        line25 = Paragraph(text, style)
        text = 'COD. VSIAF: '+str(asignacion.cod_vsiaf)
        line26 = Paragraph(text, style)
        if asignacion.chofer_id.apellido_materno is None:
            text = 'ASIGNADO A: '+asignacion.chofer_id.nombres+' '+asignacion.chofer_id.apellido_paterno+' '+' '
        else:
            text = 'ASIGNADO A: '+asignacion.chofer_id.nombres+' '+asignacion.chofer_id.apellido_paterno+' '+asignacion.chofer_id.apellido_materno
        line31 = Paragraph(text, style)
        line32 = Paragraph(' ', style)
        text = 'C.I.: '+asignacion.chofer_id.ci
        line33 = Paragraph(text, style)
        line34 = Paragraph(' ', style)
        text = 'UNIDAD: '+asignacion.unidad_id.nombre_unidad
        line35 = Paragraph(text, style)
        line36 = Paragraph(' ', style)

        data = [
            [line11, line12, line13, line14, line15, line16],
            [line21, line22, line23, line24, line25, line26],
            [line31, line32, line33, line34, line35, line36]
        ]
        table = Table(data, colWidths=(168, 50, 98, 50, 194, 148), rowHeights=(20, 20, 40))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('SPAN', (0, 2), (1, 2)),
                ('SPAN', (2, 2), (3, 2)),
                ('SPAN', (4, 2), (5, 2)),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        table.wrapOn(pdf, 700, 200)
        #Para dibujar la tabla en una posición específica del PDF, en este caso, en las coordenadas (20, 410).
        table.drawOn(pdf, 40, 360)

        pdf.setFont("Helvetica", 11)
        pdf.drawString(40, 330, u"IDENTIFICACIÓN DEL VEHÍCULO")

        style = ParagraphStyle(name='Normal')
        text = 'CLASE: '+vehiculo.clase_vehiculo
        line11 = Paragraph(text, style)
        text = 'PROCEDENCIA: '+vehiculo.procedencia
        line12 = Paragraph(text, style)
        text = 'CILINDRADA: '+str(vehiculo.cilindrada)
        line13 = Paragraph(text, style)
        text = 'MARCA: '+vehiculo.marca
        line21 = Paragraph(text, style)
        text = 'MODELO: '+str(vehiculo.modelo)
        line22 = Paragraph(text, style)
        text = 'N° MOTOR: '+vehiculo.numero_motor
        line23 = Paragraph(text, style)
        text = 'TIPO: '+vehiculo.tipo_vehiculo
        line31 = Paragraph(text, style)
        text = 'COLOR: '+vehiculo.color
        line32 = Paragraph(text, style)
        text = 'N° CHASIS: '+vehiculo.numero_chasis
        line33 = Paragraph(text, style)
        text = 'PLACA: '+vehiculo.placa
        line41 = Paragraph(text, style)
        text = 'ESTADO: '+vehiculo.estado_vehiculo
        line42 = Paragraph(text, style)
        if vehiculo.observaciones is None:
            text = 'OBSERVACIONES: '+' '
        else:
            text = 'OBSERVACIONES: '+vehiculo.observaciones
        line43 = Paragraph(text, style)

        data = [
            [line11, line12, line13],
            [line21, line22, line23],
            [line31, line32, line33],
            [line41, line42, line43]
        ]
        table = Table(data, colWidths=(230, 200, 280))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        table.wrapOn(pdf, 700, 200)
        table.drawOn(pdf, 40, 225)

    def get(self, request, *args, **kwargs):
        # Obtener el PK
        pk = self.kwargs.get('pk')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename="ReporteAsignaciónVehículo.pdf"'

        # Crear el documento PDF
        buffer = BytesIO()
        pdf = canvas.Canvas(
                buffer,                      
                pagesize=landscape((612.0, 792.0))
        )

        # Obtener los datos del modelo
        asignacion = Asignacion_Vehiculo.objects.get(pk=int(pk))
        vehiculo = asignacion.vehiculo_id

        pdf.setFont("Helvetica", 10)
        pdf.drawString(150, 40, u"BIENES INMUEBLES Y VEHÍCULOS")
        pdf.drawString(192, 25, u"SELLO Y FIRMA")

        pdf.setFont("Helvetica", 10)
        pdf.drawString(580, 40, u"Vo.Bo.")

        self.header(pdf, asignacion)
        self.tabla(pdf, 600, asignacion, vehiculo)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response

'''VISTAS PARA MECÁNICOS'''
class InicioMecanicos(TemplateView):
    template_name = 'mecanico/listaMecanicos.html'

class RegistrarMecanico(CreateView):
    model = Mecanico
    form_class = MecanicoForm
    template_name = 'mecanico/crearMecanico.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('asignacion-inicio-mecanico')

class ListadoMecanicos(ListView):
    model = Mecanico
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('asignacion-inicio-mecanico')

class EditarMecanico(UpdateView):
    model = Mecanico
    form_class = MecanicoForm
    template_name = 'mecanico/editarMecanico.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('asignacion-inicio-mecanico')

class EliminarMecanico(DeleteView):
    model = Mecanico
    template_name = 'mecanico/eliminarMecanico.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            chofer = self.get_object()
            chofer.estado = False
            chofer.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('asignacion-inicio-mecanico')

'''VISTAS PARA ORDEN DE CAMBIO DE ACEITE'''
class InicioCambioAceite(TemplateView):
    template_name = 'cambioaceite/listaCambioAceite.html'

class RegistrarCambioAceite(CreateView):
    model = Cambio_Aceite
    form_class = CambioAceiteForm
    template_name = 'cambioaceite/crearCambioAceite.html'
    success_url = reverse_lazy('asignacion-index-cambioaceite')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('asignacion-inicio-cambioaceite')

class ListadoCambioAceite(ListView):
    model = Cambio_Aceite
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('asignacion-inicio-cambioaceite')

class CambioAceiteDetailView(DetailView):
    model = Cambio_Aceite
    template_name = 'cambioaceite/detalleCambioAceite.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cambioaceite = self.model.objects.get(id = self.kwargs['pk'])
        if cambioaceite.cambio_filtros:
            cambioaceite.cambio_filtros = "Sí"
        else:
            cambioaceite.cambio_filtros = "No"
        if cambioaceite.aceite:
            cambioaceite.aceite = "Sí"
        else:
            cambioaceite.aceite = "No"
        if cambioaceite.caja:
            cambioaceite.caja = "Sí"
        else:
            cambioaceite.caja = "No"
        if cambioaceite.corona:
            cambioaceite.corona = "Sí"
        else:
            cambioaceite.corona = "No"
        if cambioaceite.engrase:
            cambioaceite.engrase = "Sí"
        else:
            cambioaceite.engrase = "No"
        if cambioaceite.aprobado:
            cambioaceite.aprobado = "Sí"
        else:
            cambioaceite.aprobado = "No"
        
        context['cambioaceite'] = cambioaceite
        return context

class EditarCambioAceite(UpdateView):
    model = Cambio_Aceite
    form_class = CambioAceiteForm
    template_name = 'cambioaceite/editarCambioAceite.html'
    success_url = reverse_lazy('asignacion-index-cambioaceite')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('asignacion-inicio-cambioaceite')

class ReporteCambioAceite(View):
    def border(self,pdf):
        pdf.roundRect(20,155,752,430,4,stroke=1, fill=0)
        pdf.roundRect(16,150,760,440,4,stroke=1, fill=0)

    def header(self, pdf):
        archivo_imagen = settings.MEDIA_ROOT+'/images/logo.png'
        imagen_auto = settings.MEDIA_ROOT+'/images/autopdf.png'
        imagen_escudob = settings.MEDIA_ROOT+'/images/escudo_boliviajpg.jpg'
        pdf.drawImage(imagen_escudob, 30, 505, 110, 80,preserveAspectRatio=True)  
        pdf.setFont("Helvetica", 10)
        pdf.drawString(170, 560, u"GOBIERNO AUTÓNOMO DEPARTAMENTAL DE POTOSÍ")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(145, 540, u"SECRETARÍA DEPARTAMENTAL ADMINISTRATIVA Y FINANCIERA")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(178, 520, u"ACTIVOS FIJOS - BIENES INMUEBLES Y SERVICIOS")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(300, 480, u"ORDEN DE CAMBIO DE ACEITE")  
        pdf.drawImage(archivo_imagen, 650, 495, 110, 80,preserveAspectRatio=True)
        pdf.drawImage(imagen_auto, 540, 446, 110, 80,preserveAspectRatio=True)
        self.border(pdf)

    def tabla(self,pdf,y,cambioaceite,vehiculo):
        style = ParagraphStyle(name='Normal')
        text = 'VEHÍCULO'
        line11 = Paragraph(text, style)
        text = 'PLACA'
        line12 = Paragraph(text, style)
        text = 'MARCA'
        line13 = Paragraph(text, style)
        text = 'MODELO'
        line14 = Paragraph(text, style)
        text = 'COLOR'
        line15 = Paragraph(text, style)
        text = vehiculo.clase_vehiculo
        line21 = Paragraph(text, style)
        text = vehiculo.placa
        line22 = Paragraph(text, style)
        text = vehiculo.marca
        line23 = Paragraph(text, style)
        text = str(vehiculo.modelo)
        line24 = Paragraph(text, style)
        text = vehiculo.color
        line25 = Paragraph(text, style)

        data = [
            [line11, line12, line13, line14, line15],
            [line21, line22, line23, line24, line25]
        ]
        table = Table(data, colWidths=(162, 142, 142, 142, 122))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ]))

        table.wrapOn(pdf, 700, 100)
        #Para dibujar la tabla en una posición específica del PDF, en este caso, en las coordenadas (20, 410).
        table.drawOn(pdf, 40, 420)

        pdf.setFont("Helvetica", 12)
        pdf.drawString(346, 395, u"TIPO DE SERVICIO")

        style = ParagraphStyle(name='Normal')
        text = 'NOMBRE MECÁNICO'
        line11 = Paragraph(text, style)
        if cambioaceite.mecanico_id.ap_materno_mecanico is None:
            text = cambioaceite.mecanico_id.nombres_mecanico+' '+cambioaceite.mecanico_id.ap_paterno_mecanico+' '+' '
        else:
            text = cambioaceite.mecanico_id.nombres_mecanico+' '+cambioaceite.mecanico_id.ap_paterno_mecanico+' '+cambioaceite.mecanico_id.ap_materno_mecanico
        line13 = Paragraph(text, style)
        text = 'KM. ACTUAL'
        line21 = Paragraph(text, style)
        text = str(cambioaceite.km_actual)
        line22 = Paragraph(text, style)
        text = 'PRÓXIMO CAMBIO'
        line23 = Paragraph(text, style)
        text = str(cambioaceite.proximo_cambio)
        line24 = Paragraph(text, style)

        data = [
            [line11, line13],
            [line21, line22, line23, line24]
        ]
        table = Table(data, colWidths=(177, 177, 177, 177))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('SPAN', (1, 0), (3, 0)),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        table.wrapOn(pdf, 700, 100)
        table.drawOn(pdf, 40, 352)

        imagen_bien = settings.MEDIA_ROOT+'/images/bien.png'
        image = Image(imagen_bien, width=1.5 * inch, height=1.5 * inch)

        style = ParagraphStyle(name='Normal')
        text = 'CAMBIO FILTROS'
        line11 = Paragraph(text, style)
        if cambioaceite.cambio_filtros == True:
            line12 = image
            line12.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line12.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line12.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line12 = Paragraph(' ', style)
        text = ' '
        line13 = Paragraph(text, style)
        text = 'ACEITE N°'
        line14 = Paragraph(text, style)
        if cambioaceite.aceite == True:
            line15 = image
            line15.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line15.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line15.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line15 = Paragraph(' ', style)
        text = ' '
        line16 = Paragraph(text, style)
        text = 'CAJA'
        line21 = Paragraph(text, style)
        if cambioaceite.caja == True:
            line22 = image
            line22.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line22.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line22.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line22 = Paragraph(' ', style)
        text = 'CORONA'
        line23 = Paragraph(text, style)
        if cambioaceite.corona == True:
            line24 = image
            line24.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line24.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line24.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line24 = Paragraph(' ', style)
        text = 'ENGRASE'
        line25 = Paragraph(text, style)
        if cambioaceite.engrase == True:
            line26 = image
            line26.drawWidth = 7 # Ajustar el ancho de la imagen en la celda
            line26.drawHeight = 7 # Ajustar la altura de la imagen en la celda
            line26.hAlign = 'CENTER'  # Centrar la imagen en la celda
        else:
            line26 = Paragraph(' ', style)

        data = [
            [line11, line12, line13, line14, line15, line16],
            [line21, line22, line23, line24, line25, line26]
        ]
        table = Table(data, colWidths=(128, 118, 108, 118, 118, 118))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('SPAN', (1, 0), (2, 0)),
                ('SPAN', (4, 0), (5, 0)),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        table.wrapOn(pdf, 700, 100)
        table.drawOn(pdf, 40, 305)
    
        style = ParagraphStyle(name='Normal')
        text = 'FECHA ENTRADA'
        line11 = Paragraph(text, style)
        text = str(cambioaceite.fecha_hora_entrada)
        line12 = Paragraph(text, style)
        text = 'LUGAR REVISIÓN'
        line13 = Paragraph(text, style)
        text = cambioaceite.maestranza
        line14 = Paragraph(text, style)
        text = 'HORA DE SALIDA'
        line21 = Paragraph(text, style)
        text = str(cambioaceite.hora_salida)
        line22 = Paragraph(text, style)

        data = [
            [line11, line12, line13, line14],
            [line21, line22]
        ]
        table = Table(data, colWidths=(157, 130, 140, 282))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('SPAN', (1, 1), (3, 1)),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        table.wrapOn(pdf, 700, 100)
        table.drawOn(pdf, 40, 258)

        style = ParagraphStyle(name='Normal')
        text = 'CONDUCTOR'
        line11 = Paragraph(text, style)
        if cambioaceite.chofer_id.apellido_materno is None:
            text = cambioaceite.chofer_id.nombres+' '+cambioaceite.chofer_id.apellido_paterno+' '+' '
        else:
            text = cambioaceite.chofer_id.nombres+' '+cambioaceite.chofer_id.apellido_paterno+' '+cambioaceite.chofer_id.apellido_materno
        line12 = Paragraph(text, style)
        text = 'FIRMA'
        line13 = Paragraph(text, style)
        text = ' '
        line14 = Paragraph(text, style)
        text = 'UNIDAD'
        line21 = Paragraph(text, style)
        text = cambioaceite.unidad_id.nombre_unidad
        line22 = Paragraph(text, style)

        data = [
            [line11, line12, line13, line14],
            [line21, line22]
        ]
        table = Table(data, colWidths=(120, 242, 130, 217), rowHeights=(40, 20))
        table.setStyle(TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.20, colors.black),
                ('SPAN', (1, 1), (3, 1)),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        table.wrapOn(pdf, 700, 100)
        table.drawOn(pdf, 40, 185)

    def get(self, request, *args, **kwargs):
        # Obtener el PK
        pk = self.kwargs.get('pk')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename="ReporteCambioAceite.pdf"'

        # Crear el documento PDF
        buffer = BytesIO()
        pdf = canvas.Canvas(
                buffer,                      
                pagesize=landscape((612.0, 792.0))
        )

        # Obtener los datos del modelo
        cambioaceite = Cambio_Aceite.objects.get(pk=int(pk))
        vehiculo = cambioaceite.vehiculo_id

        pdf.setFont("Helvetica", 10)
        pdf.drawString(150, 30, u"AUTORIZADO")

        pdf.setFont("Helvetica", 10)
        pdf.drawString(580, 30, u"VO.BO.")

        self.header(pdf)
        self.tabla(pdf, 600, cambioaceite, vehiculo)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response

