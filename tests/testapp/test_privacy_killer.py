from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from django.test.utils import override_settings

from privacy_killer.templatetags.privacy_killer import (
    privacy_killer_body, privacy_killer_head,
)


@override_settings(
    PRIVACY_KILLER_IDS=[],
)
class NotUsed(TestCase):
    def test_tag(self):
        self.assertEqual(
            privacy_killer_head(),
            '',
        )
        self.assertEqual(
            privacy_killer_body(),
            '',
        )


@override_settings(
    PRIVACY_KILLER_IDS=['GTM-bla'],
)
class GTM(TestCase):
    def test_tag(self):
        self.assertIn(
            '<!-- Google Tag Manager -->\n<script>',
            privacy_killer_head(),
        )
        self.assertIn(
            '<!-- Google Tag Manager (noscript) -->',
            privacy_killer_body(),
        )


@override_settings(
    PRIVACY_KILLER_IDS=['UA-bla'],
)
class Analytics(TestCase):
    def test_tag(self):
        self.assertIn(
            '<!-- Google Analytics -->\n<script>',
            privacy_killer_head(),
        )
        self.assertEqual(
            privacy_killer_body(),
            '',
        )
