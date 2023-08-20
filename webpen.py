import requests
import subprocess
import whois
import socket
import re

def gather_information(target_url):
    try:
        # WHOIS Lookup
        whois_result = whois.whois(target_url)
        print("WHOIS Information:")
        print(whois_result)

        # DNS Resolution
        ip_address = socket.gethostbyname(target_url)
        print("\nDNS Resolution:")
        print(f"IP Address: {ip_address}")
    except Exception as e:
        print(f"Error gathering information: {e}")


def perform_scan(target_url):
    try:
        # Run Nmap scan
        command = ["nmap", "-p-", "--min-rate", "1000", target_url]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        scan_output = result.stdout
        return scan_output
    except Exception as e:
        return f"Error performing Nmap scan: {e}"


def perform_vulnerability_assessment(target_url):
    try:
        # Run Nikto vulnerability scan
        command = ["nikto", "-h", target_url]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        scan_output = result.stdout
        return scan_output
    except Exception as e:
        return f"Error performing vulnerability assessment: {e}"

def manual_security_assessment(target_url):
    try:
        # Retrieve HTML content of the target URL
        response = requests.get(target_url)
        html_content = response.text

        # Search for potential SQL injection patterns in HTML source code
        sql_injection_patterns = ["sql error", "database error", "syntax error"]
        potential_vulnerabilities = []

        for pattern in sql_injection_patterns:
            if re.search(pattern, html_content, re.IGNORECASE):
                potential_vulnerabilities.append(pattern)

        return potential_vulnerabilities
    except Exception as e:
        return f"Error performing manual security assessment: {e}"

def perform_web_app_testing(target_url):
    try:
        # Example: Check for XSS vulnerability
        payload = "<script>alert('XSS')</script>"
        response = requests.get(target_url + "?param=" + payload)
        if payload in response.text:
            print("XSS vulnerability detected")
        else:
            print("No XSS vulnerability detected")
    except Exception as e:
        print(f"Error performing web app testing: {e}")

def perform_authentication_testing(target_url):
    try:
        # Example: Test weak authentication mechanism
        username = "admin"
        password = "password123"
        login_data = {"username": username, "password": password}
        response = requests.post(target_url + "/login", data=login_data)

        if "Welcome, admin!" in response.text:
            print("Authentication bypassed")
        else:
            print("Authentication mechanism seems secure")
    except Exception as e:
        print(f"Error performing authentication testing: {e}")

def perform_session_management_testing(target_url):
    try:
        # Example: Test session fixation vulnerability
        session_cookie = {"session_id": "attacker_session_id"}
        response = requests.get(target_url, cookies=session_cookie)

        if "Welcome, attacker!" in response.text:
            print("Session fixation vulnerability detected")
        else:
            print("Session fixation seems secure")
    except Exception as e:
        print(f"Error performing session management testing: {e}")

def perform_business_logic_testing(target_url):
    try:
        # Example: Test business logic vulnerability
        payload = "1 UNION SELECT username, password FROM users"
        response = requests.get(target_url + "?product_id=" + payload)

        if "admin" in response.text and "hashed_password" in response.text:
            print("Business logic vulnerability detected")
        else:
            print("Business logic seems secure")
    except Exception as e:
        print(f"Error performing business logic testing: {e}")

def perform_api_testing(target_url):
    try:
        # Example: Test API endpoint for security vulnerabilities
        api_endpoint = "https://example.com/api/v1/user/1"
        response = requests.get(api_endpoint)

        if response.status_code == 200 and "user_data" in response.json():
            print("API endpoint seems secure")
        else:
            print("Potential API vulnerability detected")
    except Exception as e:
        print(f"Error performing API testing: {e}")

def perform_external_services_testing(target_url):
    try:
        # Example: Test integration with third-party service
        third_party_url = "https://thirdparty.com"
        response = requests.get(third_party_url)

        if response.status_code == 200 and "sensitive_data" in response.text:
            print("External service integration may expose sensitive data")
        else:
            print("External service integration seems secure")
    except Exception as e:
        print(f"Error performing external services testing: {e}")

def perform_social_engineering_testing(target_url):
    try:
        # Example: Simulate phishing email
        email_subject = "Important Account Update Required"
        email_content = "Click the link to update your account: " + target_url
        print(f"Sending phishing email:\nSubject: {email_subject}\nContent: {email_content}")
    except Exception as e:
        print(f"Error performing social engineering testing: {e}")

def generate_report(report_content):
    try:
        with open("penetration_test_report.txt", "w") as report_file:
            report_file.write(report_content)
        print("Report generated successfully")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    target_url = input("Enter the target URL: ")

    print("\nPerforming Penetration Testing on:", target_url)

    gather_information(target_url)
    scan_output = perform_scan(target_url)
    vulnerability_assessment_output = perform_vulnerability_assessment(target_url)
    manual_security_output = manual_security_assessment(target_url)
    web_app_output = perform_web_app_testing(target_url)
    authentication_output = perform_authentication_testing(target_url)
    session_management_output = perform_session_management_testing(target_url)
    business_logic_output = perform_business_logic_testing(target_url)
    api_testing_output = perform_api_testing(target_url)
    external_services_output = perform_external_services_testing(target_url)
    social_engineering_output = perform_social_engineering_testing(target_url)

    # Generate a comprehensive report
    report_content = f"""
    Penetration Test Report
    -----------------------
    Date: 2023-08-20
    Target URL: {target_url}
    
    1. Information Gathering:
    --------------------------
    [WHOIS Information]
    ...
    [DNS Resolution]
    ...

    2. Network Scanning and Enumeration:
    ------------------------------------
    {scan_output}
    
    3. Vulnerability Assessment:
    ----------------------------
    {vulnerability_assessment_output}
    
    4. Manual Security Assessment:
    ------------------------------
    {manual_security_output}
    
    5. Web Application Testing:
    ---------------------------
    {web_app_output}
    
    6. Authentication Testing:
    --------------------------
    {authentication_output}
    
    7. Session Management Testing:
    ------------------------------
    {session_management_output}
    
    8. Business Logic Testing:
    --------------------------
    {business_logic_output}
    
    9. API Testing:
    ---------------
    {api_testing_output}
    
    10. External Services Testing:
    ------------------------------
    {external_services_output}
    
    11. Social Engineering Testing:
    ------------------------------
    {social_engineering_output}
    
    End of Report
    """

    print("\nGenerating Report...")
    generate_report(report_content)

if __name__ == "__main__":
    main()
