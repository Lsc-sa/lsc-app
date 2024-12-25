# Legal Support Center (LSC) App

The Legal Support Center (LSC) App is a Frappe-based application that provides comprehensive legal support management features. This document details the steps for installing and setting up the LSC App on a Frappe instance, including all dependencies.

---

## Prerequisites

Before starting the installation, ensure the following are installed on your system:

- **Python**: Version 3.10+
- **Node.js**: Version 16+
- **Redis**: For caching and real-time updates
- **MariaDB**: Version 10.6+
- **Yarn**
- **Bench**: Frappe CLI tool

Ensure a clean Ubuntu-based environment for optimal results.

---

## Installation Steps

### 1. Install Bench

Install Bench, the CLI tool for managing Frappe and ERPNext installations:

```bash
sudo apt update
sudo apt install python3-dev python3-setuptools python3-pip redis-server software-properties-common mariadb-server
sudo pip3 install frappe-bench
bench init frappe-bench --frappe-branch version-14
cd frappe-bench
```

### 2. Set Up MariaDB

Configure MariaDB for the Frappe environment:

1. Open the MariaDB configuration file:
   ```bash
   sudo nano /etc/mysql/my.cnf
   ```

2. Add the following under `[mysqld]`:
   ```
   character-set-client-handshake = FALSE
   character-set-server = utf8mb4
   collation-server = utf8mb4_unicode_ci
   ```

3. Restart MariaDB:
   ```bash
   sudo systemctl restart mariadb
   ```

4. Secure the installation:
   ```bash
   sudo mysql_secure_installation
   ```

5. Create a MariaDB user for Frappe:
   ```bash
   mysql -u root -p
   CREATE USER 'frappe'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON *.* TO 'frappe'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

### 3. Create a New Site

Create a new Frappe site:

```bash
bench new-site yoursite.localhost
```

Follow the prompts to set up the site.

### 4. Install Required Apps

Install the following apps in your Frappe environment:

#### Frappe Framework
```bash
bench get-app --branch version-14 frappe https://github.com/frappe/frappe.git
bench install-app frappe
```

#### ERPNext
```bash
bench get-app --branch version-14 erpnext https://github.com/frappe/erpnext.git
bench install-app erpnext
```

#### Payments
```bash
bench get-app --branch version-14 payments https://github.com/frappe/payments.git
bench install-app payments
```

#### Frappe HR
```bash
bench get-app --branch version-14 hrms https://github.com/frappe/hrms.git
bench install-app hrms
```

#### KSA VAT
```bash
bench get-app ksa_vat https://github.com/ahmadpak/ksa_vat.git
bench install-app ksa_vat
```

#### Marley Health
```bash
bench get-app marley https://github.com/earthians/marley.git
bench install-app marley
```

### 5. Install the LSC App

Install the LSC App from the Solvfast repository:

```bash
bench get-app lsc-app https://github.com/solvfast/lsc-app.git
bench install-app lsc-app
```

### 6. Start the Server

Start the Frappe development server:

```bash
bench start
```

Access your site by navigating to `http://yoursite.localhost` in your browser.

---

## Post-Installation Setup

1. Log in to your Frappe instance.
2. Configure users, roles, and permissions.
3. Set up the required modules and workflows as per your organization's needs.

---

## Support

For any issues or inquiries, please contact [Solvfast Support](mailto:support@solvfast.com).

---

## License

The LSC App is licensed under the MIT License. See the LICENSE file for details.
