import qrcode

# Image URL (this can be your own hosted image)
image_url = "https://maps.app.goo.gl/fPyXt2qge7tXisqu8"

# Generate QR code
qr = qrcode.make(image_url)

# Save QR code to file
qr.save("qr_code_image.png")

print("QR code generated and saved as 'qr_code_image.png'")
