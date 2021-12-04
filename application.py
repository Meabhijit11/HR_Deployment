from flask import Flask, request, render_template
import pickle as pk
import numpy as np

# Flask constructor
application = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@application.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        Age = float(request.form.get("Age"))
        # getting input with name = lname in HTML form
        Distance_From_Home = float(request.form.get("Distance From Home"))
        Education = request.form.get("Education")
        EnvironmentSatisfaction = request.form.get("EnvironmentSatisfaction")
        JobInvolvement = request.form.get("JobInvolvement")
        JobLevel = request.form.get("JobLevel")
        JobSatisfaction = request.form.get("JobSatisfaction")
        MonthlyIncome = float(request.form.get("MonthlyIncome"))
        NumCompaniesWorked = request.form.get("NumCompaniesWorked")
        PercentSalaryHike = float(request.form.get("PercentSalaryHike"))
        PerformanceRating = request.form.get("PerformanceRating")
        RelationshipSatisfaction = request.form.get("RelationshipSatisfaction")
        TotalWorkingYears = request.form.get("TotalWorkingYears")
        TrainingTimesLastYear = request.form.get("TrainingTimesLastYear")
        WorkLifeBalance = request.form.get("WorkLifeBalance")
        YearsAtCompany = float(request.form.get("YearsAtCompany"))
        YearsInCurrentRole = float(request.form.get("YearsInCurrentRole"))
        YearsSinceLastPromotion = float(request.form.get("YearsSinceLastPromotion"))
        YearsWithCurrManager = float(request.form.get("YearsWithCurrManager"))
        BusinessTravel_Travel_Frequently = request.form.get("BusinessTravel_Travel_Frequently")
        BusinessTravel_Travel_Rarely = request.form.get("BusinessTravel_Travel_Rarely")
        Department = request.form.get("Department")
        EducationField = request.form.get("EducationField")
        Gender = request.form.get("Gender")
        JobRole = request.form.get("JobRole")
        MaritalStatus = request.form.get("MaritalStatus")
        OverTime = request.form.get("OverTime")
        filename = r'HR_Attrition_2.pkl'
        loaded_model = pk.load(open(filename, 'rb'))
        if Department == "Research & Development":
            REDEV = 1
            Department_Sales=0
        else:
            REDEV = 0
            Department_Sales=1

        if EducationField == "Life Sciences":
            LS=1;
            MR=0;
            MD=0;
            OT=0;
            TD=0;
        elif EducationField == "Marketing":
            LS=0;
            MR=1;
            MD=0;
            OT=0;
            TD=0;
        elif Education == "Medical":
            LS=0;
            MR=0;
            MD=1;
            OT=0;
            TD=0;
        elif Education== "Other":
            LS=0;
            MR=0;
            MD=0;
            OT=1;
            TD=0;
        else:
            LS=0;
            MR=0;
            MD=0;
            OT=0;
            TD=1;

        if Gender == "Male":
            Male = 1
            Female=0
        else :
            Male = 0
            Female=1

        if JobRole == "Human Resources":
            HR=1;
            LAB=0;
            MAN=0;
            MD=0;
            RD=0;
            RS=0;
            SE=0;
            SR=0;
        elif JobRole == "Laboratory Technician":
            HR=0;
            LAB=1;
            MAN=0;
            MD=0;
            RD=0;
            RS=0;
            SE=0;
            SR=0;
        elif JobRole == "Manager":
            HR=0;
            LAB=0;
            MAN=1;
            MD=0;
            RD=0;
            RS=0;
            SE=0;
            SR=0;
        elif JobRole== "Manufacturing Director":
            HR=0;
            LAB=0;
            MAN=0;
            MD=1;
            RD=0;
            RS=0;
            SE=0;
            SR=0;
        elif JobRole == "Research Director":
            HR=0;
            LAB=0;
            MAN=0;
            MD=0;
            RD=1;
            RS=0;
            SE=0;
            SR=0;
        elif JobRole == "Research Scientist":
            HR=0;
            LAB=0;
            MAN=0;
            MD=0;
            RD=0;
            RS=1;
            SE=0;
            SR=0;
        elif JobRole== "Sales Executive":
            HR=0;
            LAB=0;
            MAN=0;
            MD=0;
            RD=0;
            RS=0;
            SE=1;
            SR=0;
        else:
            HR=0;
            LAB=0;
            MAN=0;
            MD=0;
            RD=0;
            RS=0;
            SE=0;
            SR=1;

        if MaritalStatus=="Married":
            MAR=1;
            UNMAR=0;
        else:
            MAR=0;
            UNMAR=1;

        if OverTime=="Yes":
            ys=1;
            no=0;
        else:
            ys=0;
            no=1;

        predictionresult = loaded_model.predict([[Age,Distance_From_Home,Education,EnvironmentSatisfaction,JobInvolvement,JobLevel,JobSatisfaction,MonthlyIncome,NumCompaniesWorked,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager,BusinessTravel_Travel_Frequently,BusinessTravel_Travel_Rarely,REDEV,Department_Sales,LS,MR,MD,OT,TD,Male,HR,LAB,MAN,MD,RD,RS,SE,SR,MAR,UNMAR,ys]])
        print("Prediction is ",predictionresult)
        return "Attribution Prediction of Candidate is" + str(predictionresult)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

# int(np(predictionresult[0]))