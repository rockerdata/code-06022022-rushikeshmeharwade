from os.path import exists
import sys
import json
import pandas as pd


class BMICalculator:
    def __init__(self, user_json_content):
        """Constructor for BMI Calculator. This will take user details as input

        Args:
            user_json_content (str): JSON string containing multiple user details
        """
        self._load_user_json_data(user_json_content)

    def _load_user_json_data(self, user_json_content):
        """Loads user json data as DataFrame

        Args:
            user_json_content (str): [description]
        """
        try:
            self.parameters_df = pd.DataFrame.from_dict(json.loads(user_json_content))
        except Exception as e:
            print('load_user_json_data Error in parsing CSV file ' + str(e))

    def _get_bmi_category_and_health_risk(self, bmi):
        """Generates bmi cateogry and health risk based on bmi value

        Args:
            bmi (float): BMI value

        Returns:
            tuple: A tuple containing bmi category and health risk
        """
        if (bmi < 18.5):
            return ('Underweight', 'Malnutrition risk')
        elif ((bmi >= 18.5) and (bmi < 25)):
            return ('Normal weight', 'Low risk')
        elif ((bmi >= 25) and (bmi < 30)):
            return ('Overweight', 'Enhanced risk')
        elif ((bmi >= 30) and (bmi < 35)):
            return ('Moderately obese', 'Medium risk')
        elif ((bmi >= 35) and (bmi < 40)):
            return ('Severely obese', 'High risk')
        elif ((bmi >= 40)):
            return ('Very severely obese', 'Very high risk')

    def _calculate_bmi(self, user_data):
        """This function calculates bmi value using height and weight

        Args:
            user_data (Series): Series containing single user data like height and weight

        Returns:
            float: bmi value
        """
        if user_data['HeightCm'] == 0:
            return 0
        return user_data['WeightKg'] / (user_data['HeightCm'] / 100) ** 2

    def calculate_bmi_all(self):
        """This function adds bmi category and health risk data to parameters dataframe
        """
        self.parameters_df['bmi'] = self.parameters_df.apply(self._calculate_bmi, axis=1)
        health_risk = self.parameters_df.bmi.apply(self._get_bmi_category_and_health_risk)
        self.parameters_df['bmi_category'] = list(map(lambda x: x[0], health_risk.values))
        self.parameters_df['health_risk'] = list(map(lambda x: x[1], health_risk.values))

    def overweight_count(self):
        """Calcuate overweight people in existing dataframe

        Returns:
            int: Count of overweight people
        """
        return self.parameters_df[self.parameters_df.bmi_category == 'Overweight'].shape[0]

    def dump_bmi_dataframe(self, file_name):
        """Dumps dataframe to CSV

        Args:
            file_name (str): Name of the file without extension
        """
        self.parameters_df.to_csv(file_name + ".csv")



