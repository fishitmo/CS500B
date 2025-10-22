class LoggerMixing:
    def save(self):
        print("[Log] Saving data...")
        super().save()
        

class ValidationMixing:
    def save(self):
        print("[Validation] Validating data...")
        super().save()
        
# class Database:
#     def save(self):
#         print("[Database] Saving data...")
        
class Model(LoggerMixing, ValidationMixing):
    def save(self):
        print("[Model] Saving data...")
        super().save()
        
        
m = Model()
m.save()