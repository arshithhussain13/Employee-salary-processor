class EmployeeSalaryProcessor:
    def _init_(self):
        self.salary_details = {}
    
    def validate_records(self, sr):
        
        if not all(i in sr for i in("emp_id","salary","status")):
           return False
           
        try:
            int(sr["salary"])
        
        except ValueError:
            return False
        
        if sr["status"] not in ("paid","deduct"):
            return False
            
        return True
    
    def process_records(self, sr):
        emp_id = sr["emp_id"]
        salary = int(sr["salary"])
        
        if emp_id not in self.salary_details:
            self.salary_details[emp_id] = 0
        
        if sr["status"] == "paid":
            self.salary_details[emp_id] += salary
        else:
            self.salary_details[emp_id] -= salary
            
    def process_all(self, sr):
        for sr in emp_details:
            if self.validate_records(sr):
                self.process_records(sr)
                
    def higher_salary(self):
        for emp_id, salary in self.salary_details.items():
            if salary > 50000:
                return emp_id, salary
                
emp_details = [{"emp_id":101,"salary":"20000","status":"paid"},
              {"emp_id":102,"salary":"50000","status":"deduct"},
              {"emp_id":103,"salary":"10000","status":"paid"},
              {"emp_id":104,"salary":"70000","status":"deduct"},
              {"emp_id":105,"salary":"80000","status":"paid"}]
          
processor = EmployeeSalaryProcessor()
processor.process_all(emp_details)
print("salary:",processor.salary_details)
print("Higher_salary:",processor.higher_salary())