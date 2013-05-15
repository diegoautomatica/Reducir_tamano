#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Clutter
import os
import sys

class GUI(Clutter.Stage):

    def __init__(self):
	Clutter.Stage.__init__(self)
        self.set_title("Programa Tonto para Sole")

        self.box=Clutter.Box();
        self.boxorder=Clutter.BoxLayout()
        self.boxorder.set_vertical(True)
        self.box.set_layout_manager(self.boxorder)
        self.add_actor(self.box)

        self.escoger=Clutter.Text()
        self.escoger.set_text("Escoja imágenes")
#        self.escoger.connect("clicked", self.escoger_clicked)
        self.box.add_actor(self.escoger)
#        self.caja.pack_start(self.escoger, True, True, 0)
#        
#        self.lista = Gtk.ListStore(str)
#        self.vistalista=Gtk.TreeView(self.lista);
#        self.renderer_text = Gtk.CellRendererText()
#        self.column_text = Gtk.TreeViewColumn("",self.renderer_text, text=0)
#        self.vistalista.append_column(self.column_text)        
#        self.caja.pack_start(self.vistalista, True, True, 0);
#        
#        self.caja.pack_start(Gtk.Separator(),True,True,0);
#        
#        self.etiqueta=Gtk.Label("Porcentaje a reducir");
#        self.caja.pack_start(self.etiqueta,True,True,0);
#        
#        
#        
#        self.escala=Gtk.Scale();
#        #self.escala.set_orientation(GTK_ORIENTATION_HORIZONTAL)
#        self.escala.set_range(1,100);
#        self.escala.set_digits(0);
#        self.escala.set_value(10);
#        self.caja.pack_start(self.escala,True,True,0);
#        
#        self.convertir = Gtk.Button(label="Convertir las imagenes")
#        self.convertir.connect("clicked", self.convertir_clicked)
#        self.caja.pack_start(self.convertir, True, True, 0)

#        self.progreso=Gtk.ProgressBar();
#        self.progreso.set_fraction(0.0);
#        self.progreso.set_Visible=False;
#        self.caja.pack_start(self.progreso, True, True, 0);

#    def escoger_clicked(self, widget):
#        dialog = Gtk.FileChooserDialog("Escoja las imagenes", self,
#            Gtk.FileChooserAction.OPEN,
#            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
#             Gtk.STOCK_OPEN, Gtk.ResponseType.OK));
#        dialog.set_select_multiple(True);
#        filter_image = Gtk.FileFilter()
#        filter_image.set_name("Imágenes")
#        filter_image.add_mime_type("image/*")
#        dialog.add_filter(filter_image)
#        response = dialog.run();
#        if response == Gtk.ResponseType.OK:
#            for fichero in dialog.get_filenames():
#                self.lista.append([fichero]);
#        #print self.vistalista.get_column(0).get_name();
#        dialog.destroy();
#        
#    def convertir_clicked(self, widget):
#        tamano=len(self.lista); cuenta=0.0;
#        for fichero in self.lista:
#            #os.system("convert a.jpg b.jpg");
#            nombre=fichero[:][0];
#            sinext=nombre[:-4];
#            os.system("convert -resize "+str(self.escala.get_value())+"% "+nombre+" "+ sinext+"convertida.jpg");
#            cuenta=cuenta+1.0;
#            self.progreso.set_fraction(1.0*cuenta/tamano);
#            print 1.0*cuenta/tamano;
Clutter.init(sys.argv)
ventana = GUI()
ventana.connect('destroy', lambda x: Clutter.main_quit() )
ventana.show_all()
Clutter.main()
