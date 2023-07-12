class ContractGenerator:
    def __init__(self, sport):
        self.sport = sport

    def generate_contract_template(self, contract_type):
        if self.sport == "football":
            if contract_type == "rookie":
                return self.generate_rookie_contract_template()
            elif contract_type == "veteran":
                return self.generate_veteran_contract_template()
            else:
                raise ValueError("Invalid contract type")
        elif self.sport == "basketball":
            if contract_type == "rookie":
                return self.generate_rookie_contract_template()
            elif contract_type == "veteran":
                return self.generate_veteran_contract_template()
            else:
                raise ValueError("Invalid contract type")
        else:
            raise ValueError("Invalid sport")

    def generate_rookie_contract_template(self):
        # Generate rookie contract template
        template = {
            "contract_type": "rookie",
            "salary": 0,
            "contract_duration": 4,
            "bonus": 0,
            "salary_cap_impact": 0,
            "contract_value": 0
        }
        return template

    def generate_veteran_contract_template(self):
        # Generate veteran contract template
        template = {
            "contract_type": "veteran",
            "salary": 0,
            "contract_duration": 1,
            "bonus": 0,
            "salary_cap_impact": 0,
            "contract_value": 0
        }
        return template

    def customize_contract_terms(self, contract_template, salary, contract_duration, bonus):
        # Customize contract terms based on player and team requirements
        contract_template["salary"] = salary
        contract_template["contract_duration"] = contract_duration
        contract_template["bonus"] = bonus

        # Calculate contract-related metrics
        contract_template["salary_cap_impact"] = self.calculate_salary_cap_impact(salary)
        contract_template["contract_value"] = self.calculate_contract_value(salary, contract_duration, bonus)

        return contract_template

    def calculate_salary_cap_impact(self, salary):
        # Calculate salary cap impact
        salary_cap_impact = salary * 0.1  # Assuming 10% salary cap impact
        return salary_cap_impact

    def calculate_contract_value(self, salary, contract_duration, bonus):
        # Calculate contract value
        contract_value = salary * contract_duration + bonus
        return contract_value


# Example usage
contract_generator = ContractGenerator("football")
contract_template = contract_generator.generate_contract_template("rookie")
customized_contract = contract_generator.customize_contract_terms(contract_template, 1000000, 4, 50000)

print(customized_contract)