# Report Generation Internal Guidelines and Structured Knowledge

## I. Foundational Knowledge: Quantum Computing Threats

### A. Core Quantum Threat to Cryptography
The primary threat stems from **Shor's Algorithm**. This algorithm can efficiently break the most common public-key encryption schemes currently used worldwide, specifically:
* **RSA (Rivest–Shamir–Adleman):** Used for secure communication, digital signatures, and key exchange.
* **Elliptic Curve Cryptography (ECC):** Used widely in TLS/SSL, digital wallets, and VPNs.
* **Diffie-Hellman Key Exchange:** Used for establishing shared secret keys.
    This threat is generally referred to as the **"Q-Day"** scenario.

### B. The 'Harvest Now, Decrypt Later' Risk
This is the immediate, non-quantum risk. Threat actors can intercept and store large volumes of encrypted data today. When a sufficiently powerful fault-tolerant quantum computer (FTQC) is operational, they can decrypt all this harvested data.

## II. Post-Quantum Cryptography (PQC) Mitigation Strategies

### A. NIST Standardization Update (Internal Policy)
Our current internal policy aligns with the NIST Post-Quantum Cryptography Standardization effort. The primary goal is to transition all systems to **NIST-selected** PQC algorithms within the next three years (by 2028).

* **Key Establishment Mechanism:** We prioritize **CRYSTALS-Kyber** for secure key exchange, as it is robust and the primary selection by NIST.
* **Digital Signature Algorithm:** We are evaluating **CRYSTALS-Dilithium** for digital signatures, but will maintain a 'hybrid mode' during the transition period.

### B. Internal Mitigation Phases (The Cryptographic Inventory Roadmap)

| Phase | Goal | Focus | Timeline |
| :--- | :--- | :--- | :--- |
| **Phase 1: Discovery** | Create a complete cryptographic inventory. | Identify all instances of vulnerable crypto (RSA, ECC), their locations (servers, IoT, endpoints), and the type of data protected. | Current Year |
| **Phase 2: Prioritization**| Deploy pilot PQC solutions. | Focus on high-risk, long-confidentiality-lifetime data and key exchange infrastructure (e.g., root CAs, VPN gateways). Use **Hybrid Mode**. | Next 1-2 Years |
| **Phase 3: Migration** | Full transition to PQC standards. | Deploy PQC across the entire enterprise, eliminating all classical vulnerable algorithms. | 2028 |

**Key Internal Term:** **Hybrid Mode** refers to running a classical algorithm (like ECC) in parallel with a PQC algorithm (like Kyber) to provide security resilience against both classical and potential PQC vulnerabilities during the transition.