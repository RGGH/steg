from stegano import lsb

def hide_text_in_image(image_path, text_to_hide, output_path):
    """Hides text inside an image using LSB steganography."""
    secret_image = lsb.hide(image_path, text_to_hide)
    secret_image.save(output_path)

def read_text_from_image(image_path):
    """Reads hidden text from an image using LSB steganography."""
    secret_text = lsb.reveal(image_path)
    return secret_text

if __name__ == "__main__":
    # Replace these paths with your own image and lightning address
    input_image_path = "www.png"
    lightning_address = "lntb1599n1pjtnzkgpp59m8jv6jaxhxjsqyrn8ch754uaxqujapwah7tnh7lx9s0deqgd5qsdpa2fjkzep6yp58garswvaz7tm5v4ehgmn9wsh8jctvd3ejummjvuhjqum5w4cxjcqzysxqr23ssp5lpxre3c70eetf4v6xat3m4sr6rulkrfvstn4nqf9wynzs3h5jnhs9qyyssqw8wevrzktf8gydc8cujx73h8ecx428p8fj90a2pp7gp377ch6p6ju3uaz25q8c0hpd59h8e6h9yet972amvznnhtqc3q0cw09ntjnjcputcqs0"
    output_image_path = "output_image.png"

    try:
        # Encode the lightning address in the image
        hide_text_in_image(input_image_path, lightning_address, output_image_path)
        print("Lightning address successfully encoded in the image.")

        # Decode the lightning address from the image
        decoded_lightning_address = read_text_from_image(output_image_path)
        print("Decoded Lightning Network address:", decoded_lightning_address)
    except Exception as e:
        print(f"An error occurred: {e}")

