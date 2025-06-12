from pyngrok import ngrok

# Open a public tunnel to port 5000 (Flask default)
public_url = ngrok.connect(5000)
print(f" * Ngrok tunnel available at: {public_url}")
input("Press ENTER to keep tunnel open...")