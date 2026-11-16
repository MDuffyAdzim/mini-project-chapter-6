# Desain struktur data untuk menyimpan informasi mahasiswa

students = {
    "241063117000": {
        "name": "Duffy",
        "major": "Management",
        "skills": [
            "Python", "HTML", "CSS",
                "Critical Thinking & Problem Solving", 
                "Public Speaking", 
                "Time Management", 
                "Teamwork & Collaboration",
                "Leadership"
        ]
    },

    "241063117001": {
        "name": "Nizam",
        "major": "Mathematics",
        "skills": [
            "Python", "Excel", 
                "Teamwork & Collaboration"
        ]
    },

    "241063117002": {
        "name": "Fandu",
        "major": "Marketing",
        "skills": [
            "Data Analytics", "Copywriting & Content", "Paid Advertising",
                "Critical Thinking & Problem Solving",  
                "Time Management", 
                "Teamwork & Collaboration"
        ]
    },

    "241063117003": {
        "name": "Budi",
        "major": "Accounting",
        "skills": [
            "Financial Reporting", "Financial Forecasting", "Tax Strategy", 
                "Public Speaking", 
                "Time Management"
        ]
    },
    
    "241063117004": {
        "name": "Andi",
        "major": "Law",
        "skills": [
            "Legal Research & Analysis", "Contract Drafting & Negotiation",
                "Critical Thinking & Problem Solving", 
                "Public Speaking", 
                "Time Management"
        ]
    }
}

# Kumpulan kemampuan soft skills yang diinginkan kampus untuk dimiliki mahasiswa.

demand_skill = [
    "Critical Thinking & Problem Solving", "Public Speaking", 
    "Time Management", "Teamwork & Collaboration", "Leadership"
]

# Integrasi program menjadi satu sistem yang bisa di akses bersamaan.

while True:
    print("\n" + "=" * 48)
    print("🎓        STUDENT SKILL MANAGER        🎓")
    print("=" * 48)
    print("Welcome! Please select a feature below:\n")
    print("  [1] 📋 Display All Students")
    print("  [2] 🎯 Required Campus Skills")
    print("  [3] 🔍 Check Student Skills")
    print("  [4] ✨ Display Unique Skills")
    print("  [5] 🚪 Exit Program")
    print("-" * 48)
    print("💡 Tip: Enter a number between 1 and 5.")

    # Input angka oleh user.
    # Di back up oleh function try and except agar kita bisa mencegah error-nya program karena user yang meng-inputkan data yang salah.
    # Yaitu tipe data selain integer.

    try:
        user_input_integer = int(input("👉 Enter your choice (1-5): "))
        print("\n")
    except ValueError:
        print("\n")
        print("⚠️ Oops! Numbers only. Please select a valid choice (1-5).\n")
        continue

    # 1

    # Program yang menampilkan semua mahasiswa beserta informasi pribadi-nya.

    if user_input_integer == 1:
        print("========== STUDENT SKILL MANAGER ==========")
        print("\n")
        for npm, information in students.items():
            print(f"NPM\t: {npm}")
            print(f"Name\t: {information["name"]}")
            print(f"Major\t: {information["major"]}")
            result = f'{", ".join(information["skills"])}.'
            print(f"Skills\t: {result}")        
            print("\n")
    # 2

    # Kalau ini adalah program yang menampilkan kemampuan yang diinginkan kampus agar mahasiswa punya untuk menunjang kesuksesan karir.

    elif user_input_integer == 2:
        print("\n" + "=" * 48)
        print("🎯         REQUIRED CAMPUS SKILLS           🎯")
        print("=" * 48)
        print("\n")
        print("Core competencies expected by the university:\n")
        for skill in demand_skill:
            print(f"-\t {skill}\n")        
        print("💡 Tip: Compare these with student skills!")
    
    # 3
    
    # Ini adalah program yang menge-check kemampuan yang dimiliki mahasiswa berdasarkan informasi pribadi-nya yang tercatat sistem.

    elif user_input_integer == 3:
        npm_student = input("Enter Student ID: ")
        npm_not_found = students.get(npm_student, f"NPM / {npm_student}: Not Found") 
        if npm_student not in students:
            print(f"{npm_not_found}")
            continue
        check_skills = input("Enter skill to check: ")
        print("\n")
        print("========== CHECK STUDENT SKILLS ==========")
        print("\n")
        print(f"Student NPM: {npm_student}")
        print(f"Skill to check: {check_skills}")
        print("\n")

        if check_skills in students[npm_student]["skills"]:
            print(f"{students[npm_student]["name"]} memiliki keterampilan tersebut.")
        else:
            print(f"{students[npm_student]["name"]} tidak memiliki keterampilan tersebut.")

    # 4

    # Program yang menampilkan kemampuan unik yang dimiliki mahasiswa pada kampus ini.

    elif user_input_integer == 4:
        # Tampilan untuk menginformasikan kemampuan unik yang dimiliki setiap mahasiswa pada kampus ini.  
        print("\n⚡ ==================================================================== ⚡")
        print("📢 BEYOND STANDARD: HONORING CAMPUS EXTRAORDINARY & UNIQUE ABILITIES")
        print("⚡ ==================================================================== ⚡")
        print("\n")

        # Logika yang mengiterasikan list skills agar bisa hanya di ambil kemampuan unique nya saja / tiap elemen unique saja. 

        all_skills = []
        for _, information in students.items():
            student_skills = information["skills"]
            for ability in student_skills:
                all_skills.append(ability)

        # Keberhasilan meng-unique kan setiap elemen pada kode di bawah ini, setelah menyelsaikan logika sebelumnya.

        unique_skills = sorted(set(all_skills))    

        # Kode yang mengiterasi setiap kemampuan unique untuk di tampilkan dan diinformasikan.

        print(f"🔥 Unveiling an extraordinary talent: This is the elite unique skill mastered by the campus student: ")
        print("\n")
        for unique in unique_skills:
            print(f"-\t{unique}")
        print("\n")
    
    # 5

    # Program yang mengakhiri sesi interaksi dengan program STUDENT SKILL MANAGER. 

    elif user_input_integer == 5:
        print("=" * 48)
        print("👋   THANK YOU FOR USING STUDENT SKILL MANAGER  ")
        print("      Session ended. Have a productive day!     ")
        print("=" * 48 + "\n")
        break

    # Mekanisme else yang memberikan peringatan bagi user yang menginputkan angka (Integer) selain dari 1-5.
    else:
        print("⚠️ Invalid choice. Please select a number between 1 and 5.")