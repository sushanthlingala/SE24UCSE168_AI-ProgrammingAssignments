import random
import string

class CaptchaGenerator:
    def generate(self):
        characters = string.ascii_uppercase + string.digits
        code = "".join(random.choices(characters, k=5))
        return code

    def distort(self, code):
        noise_symbols = [".", "~", "*", "|", "!"]
        distorted_chars = []
        for ch in code:
            distorted_chars.append(ch + random.choice(noise_symbols))
        distorted = " ".join(distorted_chars)
        return "[ " + distorted + " ]"

class CaptchaValidator:
    def check(self, original_code, user_input):
        return user_input.strip().upper() == original_code.upper()

class CaptchaSession:
    MAX_ATTEMPTS = 3

    def __init__(self):
        self.attempts = 0
        self.solved = False
        self.locked = False
        self.generator = CaptchaGenerator()
        self.validator = CaptchaValidator()
        self.current_code = None

    def new_challenge(self):
        self.current_code = self.generator.generate()
        return self.generator.distort(self.current_code)

    def submit(self, user_input):
        if self.locked:
            return "locked"
        self.attempts += 1
        if self.validator.check(self.current_code, user_input):
            self.solved = True
            return "correct"
        if self.attempts >= self.MAX_ATTEMPTS:
            self.locked = True
            return "locked"
        return "incorrect"

def run():
    print("--- CAPTCHA Verification ---")
    session = CaptchaSession()

    while not session.solved and not session.locked:
        challenge = session.new_challenge()
        print("\n" + challenge)
        user_input = input(
            "Enter the 5 characters shown in the CAPTCHA (without spaces): "
        )
        result = session.submit(user_input)

        if result == "correct":
            print("Access granted.")
        elif result == "locked":
            print("Too many incorrect attempts. Access denied.")
        else:
            remaining = CaptchaSession.MAX_ATTEMPTS - session.attempts
            print(f"Incorrect. {remaining} attempt(s) remaining.")

run()
