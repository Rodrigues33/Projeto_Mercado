from dis import show_code
import qrcode  

image = qrcode.make("00020126480014br.gov.bcb.pix0126paulodiniz019283@gmail.com5204000053039865802BR5925Paulo Henrique Barros Din6009Sao Paulo62070503***63049CE1")
image.save("qrc_python.png")