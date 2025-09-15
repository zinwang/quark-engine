import pytest
import requests

from quark.forensic import Forensic

APK_SOURCE = (
    "https://github.com/quark-engine/apk-samples"
    "/raw/master/malware-samples/14d9f1a92dd984d6040cc41ed06e273e.apk"
)
APK_FILENAME = "14d9f1a92dd984d6040cc41ed06e273e.apk"


@pytest.fixture()
def forensic(scope="function"):
    r = requests.get(APK_SOURCE, allow_redirects=True)
    open(APK_FILENAME, "wb").write(r.content)

    apk_file = APK_FILENAME
    forensic = Forensic(apk_file)
    yield forensic


class TestForensic:
    def test_all_strings(self, forensic):
        assert len(forensic.get_all_strings()) == 4408

    def test_get_url(self, forensic):
        assert len(forensic.get_url()) == 4
        assert "http://mmsc.vnet.mobi" in forensic.get_url()
        assert "http://mmsc.myuni.com.cn" in forensic.get_url()
        assert "http://www.google.com/loc/json" in forensic.get_url()
        assert "http://mmsc.monternet.com" in forensic.get_url()

    def test_get_ip(self, forensic):
        assert len(forensic.get_ip()) == 3
        assert "10.0.0.200" in forensic.get_ip()
        assert "114.80.208.163" in forensic.get_ip()
        assert "10.0.0.172" in forensic.get_ip()

    def test_get_content(self, forensic):
        assert len(forensic.get_content()) == 4
        assert "content://sms" in forensic.get_content()
        assert "content://telephony/carriers" in forensic.get_content()
        assert "content://sms/sent" in forensic.get_content()
        assert "content://telephony/carriers/preferapn" in forensic.get_content()

    def test_get_file(self, forensic):
        assert len(forensic.get_file()) == 0

    def test_get_base64(self, forensic):
        assert len(forensic.get_base64()) == 603

    def test_get_android_api(self, forensic):
        assert len(forensic.get_android_api()) == 828

        result = [str(x) for x in forensic.get_android_api()]
        assert any("getCellLocation" in meth for meth in result)
        assert any("sendTextMessage" in meth for meth in result)
