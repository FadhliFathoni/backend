from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BarangModel
from .serializers import BarangSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method == "POST":
        serializer = BarangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Berhasil"})
        return Response(serializer.errors, status=400)
    return Response({"message": "POST BARANG"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def allBarang(request):
    queryset = BarangModel.objects.all()
    serializer = BarangSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def oneBarang(request, id_barang):
    queryset = BarangModel.objects.filter(id=id_barang)
    serializer = BarangSerializer(queryset.first())
    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteBarang(request, id_barang):
    if request.user.is_superuser:
        try:
            barang = BarangModel.objects.get(id=id_barang)
            barang.delete()
            return Response({"message": "Success"})
        except BarangModel.DoesNotExist:
            return Response({"message": "Barang not found"}, status=404)
    else:
        return Response({"message": "You are not admin"}, status=403)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateBarang(request, id_barang):
    try:
        barang = BarangModel.objects.get(id=id_barang)
    except BarangModel.DoesNotExist:
        return Response({"message": "Barang not found"}, status=404)
    
    if request.method == "PUT":
        serializer = BarangSerializer(barang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Berhasil"})
        return Response(serializer.errors, status=400)
    serializer = BarangSerializer(barang)
    return Response(serializer.data)

class Barang(ListAPIView):
    serializer_class = BarangSerializer
    queryset = BarangModel.objects.all()