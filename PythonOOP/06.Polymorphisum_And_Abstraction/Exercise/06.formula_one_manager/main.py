from unittest import TestCase, main
from project.f1_season_app import F1SeasonApp


class TestF1SeasonAppClass(TestCase):
    def test_f1_season_app_register_invalid_team_name_should_raise_error(self):
        self.f1_season_app = F1SeasonApp()

        with self.assertRaises(ValueError) as ve:
            self.f1_season_app.register_team_for_season("Monster", 2000000)

        self.assertEqual(str(ve.exception), "Invalid team name!")


if __name__ == '__main__':
    main()