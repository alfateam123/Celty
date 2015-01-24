import unittest
import time
from celty import torrent
from celty import conf

class TestTorrentFinder(unittest.TestCase):
    def setUp(self):
        self.finder = torrent.TorrentFinder('trallallero')

    def test_listNoTorrents(self):
        finder = torrent.TorrentFinder('tests/data/no_torrents')
        self.assertEqual(list(finder.list()), [])

    def test_listTorrents(self):
        finder = torrent.TorrentFinder('tests/data/with_torrents')
        self.assertNotEqual(list(finder.list()), [])
        self.assertEqual(list(finder.list()), ["tests/data/with_torrents/nisemono.torrent"])

class TestTorrentInfo(unittest.TestCase):
    def setUp(self):
        self.conf = conf.ConfReader('tests/celty.conf')

    def test_patternFromSeriesConf_Nisekoi(self):
        self.assertEqual(
            torrent.TorrentInfo.patternFromSeriesConf(self.conf.extractShowInfo("Nisekoi")),
            "[Omnivium] Nisekoi")

    def test_patternFromSeriesConf_SoranoWoto(self):
        self.assertEqual(
            torrent.TorrentInfo.patternFromSeriesConf(self.conf.extractShowInfo("Sora no Woto")),
            "[Elysium] Sora no Woto (BD.1080p.FLAC)")
        
class TestTorrentSeriesFromPattern(unittest.TestCase):
    def setUp(self):
        self.conf = conf.ConfReader('tests/celty.conf')

    def test_seriesFromPattern_Nisekoi(self):
        self.assertEqual(
            torrent.TorrentInfo.seriesFromPattern("[Omnivium] Nisekoi", self.conf),
            self.conf.extractShowInfo("Nisekoi")
            )

    def test_seriesFromPattern_SoranoWoto(self):
        self.assertEqual(
            torrent.TorrentInfo.seriesFromPattern("[Elysium] Sora no Woto (BD.1080p.FLAC)", self.conf),
            self.conf.extractShowInfo("Sora no Woto")
            )

    def test_seriesFromPattern_unknown(self):
        self.assertRaises(
            ValueError,
            torrent.TorrentInfo.seriesFromPattern,
            pattern="[yfw] no series", conf=self.conf
            )

    def test_seriesFromPattern_realTorrentName(self):
        self.assertEqual(
            torrent.TorrentInfo.seriesFromPattern("[Akindo-SSK] Shigatsu wa Kimi no Uso - 13 [TV][720p][Sub ITA][DADB0BED].mkv.torrent", self.conf),
            self.conf.extractShowInfo("Shigatsu")
            )