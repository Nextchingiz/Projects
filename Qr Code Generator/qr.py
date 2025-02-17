#Import qrcode library
import qrcode

# Data to be encoded
data = "website url"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction used for the QR Code
    box_size=10,  # Amount of pixels each “box” of the QR code is
    border=4,  # Amount of boxes thick the border should be
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")