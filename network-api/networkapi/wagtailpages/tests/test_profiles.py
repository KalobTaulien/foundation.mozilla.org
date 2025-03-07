from django import test

from networkapi.wagtailpages.pagemodels import profiles as profile_models
from networkapi.wagtailpages.factory import research_hub as research_factory
from networkapi.wagtailpages.factory import profiles as profile_factories


class ProfileTest(test.TestCase):
    def test_factory(self):
        profile_factories.ProfileFactory()
        self.assertTrue(True)

    def test_filter_research_authors(self):
        research_author_profile = profile_factories.ProfileFactory()
        research_factory.ResearchAuthorRelationFactory(
            research_detail_page=research_factory.ResearchDetailPageFactory(),
            author_profile=research_author_profile,
        )
        not_research_author_profile = profile_factories.ProfileFactory()

        research_author_profiles = (
            profile_models.Profile.objects.filter_research_authors()
        )

        self.assertIn(research_author_profile, research_author_profiles)
        self.assertNotIn(not_research_author_profile, research_author_profiles)

    def test_filter_research_authors_distinct(self):
        ''' Return research author profile only once'''

        research_author_profile = profile_factories.ProfileFactory()
        research_factory.ResearchAuthorRelationFactory(
            research_detail_page=research_factory.ResearchDetailPageFactory(),
            author_profile=research_author_profile,
        )
        research_factory.ResearchAuthorRelationFactory(
            research_detail_page=research_factory.ResearchDetailPageFactory(),
            author_profile=research_author_profile,
        )

        profiles = profile_models.Profile.objects.all()
        profiles = profiles.filter_research_authors()
        profiles = profiles.filter(id=research_author_profile.id)
        count = profiles.count()

        self.assertEqual(count, 1)
