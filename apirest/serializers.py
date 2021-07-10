from rest_framework import serializers
from .models import LibroDiario,boleta,boletaDetalle, factura, facturaDetalle, notaDebito, notaDebitoDetalle


class LibroDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDiario
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    Debe = serializers.IntegerField()
    Haber = serializers.IntegerField()
    SaldoDeudor = serializers.IntegerField()
    SaldoAcreedor =serializers.IntegerField()

    class Meta:
        model = LibroDiario
        fields = 'id_transaccion','nombre_transaccion','Debe','Haber','SaldoDeudor','SaldoAcreedor'


class boletaDetalleSerializers(serializers.ModelSerializer):
    class Meta:
        model = boletaDetalle
        #fields = '__all__'
        fields = ("nombre_producto", "cantidad", "precio_actual")

class boletaSerializer(serializers.ModelSerializer):
    #detalle_boleta = boletaDetalleSerializers()
    detalle = boletaDetalleSerializers(many=True)

    class Meta:
        model = boleta
        fields = '__all__'

    def create(self, validated_data):
        boleta_g = boleta( id_cliente = validated_data.get("id_cliente"),
                           fecha_venta=validated_data.get("fecha_venta"),
                           neto_v = validated_data.get("neto_v"),
                           neto_c=validated_data.get("neto_c"),
                           iva_total=validated_data.get("iva_total"),
                           total_v=validated_data.get("total_v"),
                           metodo_pago = validated_data.get("metodo_pago"),
                         )
        boleta_g.save()
        detalle = validated_data.get('detalle')
        for detalles in detalle:
            boletaDetalle.objects.create(id_boleta=boleta_g, **detalles)
        return validated_data


class facturaDetalleSerializers(serializers.ModelSerializer):
    class Meta:
        model = facturaDetalle
        #fields = '__all__'
        fields = ("nombre_producto", "cantidad", "precio_actual")

class facturaSerializer(serializers.ModelSerializer):
    #detalle_boleta = boletaDetalleSerializers()
    factura_detalle = facturaDetalleSerializers(many=True)

    class Meta:
        model = factura
        fields = '__all__'

    def create(self, validated_data):
        factura_g = factura( id_cliente = validated_data.get("id_cliente"),
                           fecha_venta=validated_data.get("fecha_venta"),
                           neto_v = validated_data.get("neto_v"),
                           iva_total=validated_data.get("iva_total"),
                           total_v=validated_data.get("total_v"),
                           metodo_pago = validated_data.get("metodo_pago"),
                         )
        factura_g.save()
        factura_detalle = validated_data.get('factura_detalle')
        for detalles in factura_detalle:
            facturaDetalle.objects.create(id_factura=factura_g, **detalles)
        return validated_data