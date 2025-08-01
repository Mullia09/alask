import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from volunteer_app.main import generate_otp


def test_generate_otp_length():
    otp = generate_otp()
    assert len(otp) == 6
    assert otp.isdigit()




