## 📡 Frequency Reuse Strategy and Network Planning

### **Question.**  
An operator has **10 frequency channels** available from 900 MHz, 1800 MHz, and 1900 MHz spectrums. The goal is to serve:

- **Zone 1**: 10,000 subscribers (Radius = 25 km)  
- **Zone 2**: 15,000 subscribers (Radius = 30 km)  
- **Zone 3**: 5,000 subscribers (Radius = 15 km)  

Develop a frequency reuse plan that:
- Ensures efficient spectrum utilization  
- Minimizes **co-channel interference**  
- Maximizes **revenue and service quality**  
- Uses dynamic allocation to reduce **call drops**

---

### **Step 1: Area Calculation**

Using the formula for the area of a circle:

\[
\text{Area} = \pi R^2
\]

| Zone | Radius (km) | Area (sq. km) |
|------|-------------|----------------|
| Z1   | 25          | 1963.5         |
| Z2   | 30          | 2827.4         |
| Z3   | 15          | 706.9          |

---

### **Step 2: Subscriber Density**

\[
\text{Density} = \frac{\text{Subscribers}}{\text{Area}}
\]

| Zone | Subscribers | Area | Density (subs/km²) |
|------|-------------|------|--------------------|
| Z1   | 10,000      | 1963.5 | ≈ 5.1             |
| Z2   | 15,000      | 2827.4 | ≈ 5.3             |
| Z3   | 5,000       | 706.9  | ≈ 7.07            |

🔹 **Z1**: Semi-urban — moderate density and area  
🔹 **Z2**: Urban — largest area, moderate density  
🔹 **Z3**: Rural — highest density but smallest region

---

### **Step 3: Traffic Load Estimation**

Assumptions:
- **Avg. call duration** = 3 minutes  
- **Busy hour call attempts** = 10%  
- **Blocking probability** = 2%  
- **Traffic per subscriber** = 0.1 × 3 min = **0.005 Erlangs**

| Zone | Subscribers | Total Traffic (Erlangs) |
|------|-------------|--------------------------|
| Z1   | 10,000      | 0.005 × 10,000 = **50E** |
| Z2   | 15,000      | 0.005 × 15,000 = **75E** |
| Z3   | 5,000       | 0.005 × 5,000 = **25E**  |

From Erlang B tables (2% blocking probability):
- Z1 → ~70 channels  
- Z2 → ~90 channels  
- Z3 → ~40 channels  
→ Total Needed = **200 channels**

🛑 **Only 10 channels available** — implement **frequency reuse**

---

### **Step 4: Frequency Reuse Planning**

We use the **reuse factor (N)** from the standard GSM hexagonal cell model.

| Zone | Reuse Factor (N) | Reason |
|------|------------------|--------|
| Z1   | 4                | High capacity needed, semi-urban |
| Z2   | 7                | High traffic, urban area         |
| Z3   | 7                | Low load, rural area             |

---

### **Step 5: Channel Allocation**

**Z1 (N=4)**:  
- Channels per cell ≈ 10 / 4 = 2.5  
- Cell assignments:  
  - Cell 1 → Ch 1, 2  
  - Cell 2 → Ch 3, 4  
  - Cell 3 → Ch 5, 6  
  - Cell 4 → Ch 7, 8  
- Channels 9, 10 reserved for **dynamic allocation/load balancing**

**Z2 & Z3 (N=7)**:  
- Channels per cell ≈ 1  
- Cell assignments:  
  - Cells 1–7 → Ch 1–7  
  - Channels 8–10 reserved for dynamic sharing/load balancing

---

### **Step 6: Co-channel Interference Considerations**

| Zone | Interference Level | Comments |
|------|--------------------|----------|
| Z1   | Moderate            | Acceptable due to capacity priority |
| Z2   | Low                 | Proper spacing using N=7 |
| Z3   | Very Low            | Sparse rural layout ensures minimal interference |

---

### **Step 7: Grade of Service (GoS) & Calls Served**

| Zone | Call Attempts | Blocked (2%) | Served |
|------|---------------|--------------|--------|
| Z1   | 1000          | 20           | 980    |
| Z2   | 1500          | 30           | 1470   |
| Z3   | 500           | 10           | 490    |

---

### **Step 8: Number of Cells and Clusters**

Cell area based on standard hexagonal model:  
\[
\text{Cell Area} = \frac{3\sqrt{3}}{2} R^2
\]

| Zone | Cell Radius (km) | Cell Area (sq. km) | Total Cells | Clusters (Cells/N) |
|------|------------------|--------------------|-------------|---------------------|
| Z1   | 2                | 10.39              | ~189        | 48                  |
| Z2   | 5                | 64.95              | ~44         | 7                   |
| Z3   | 8                | 166.2              | ~5          | 1                   |


Great! Let's expand the previous answer by calculating the **number of channels per cell after sectoring**, especially in **Zone 2**, and analyze **whether the requirement is met** in terms of **traffic handling capacity**.

---

## 📶 Sectoring and Its Impact on Channel Allocation

### 🔄 What Is Cell Sectoring?

- **Sectoring** splits a cell into **3 sectors** using directional antennas, each covering 120°.
- It **reduces interference** and **increases capacity** without needing more spectrum.
- The **same frequency channel** can now be reused **three times**—once per sector.

---

## 🔢 Channel Calculation After Sectoring

Let's recalculate **channel capacity per zone**, especially focusing on **Zone 2**, which undergoes sectoring.

---

### **Zone 2: Sectoring Applied (N = 7)**

#### Before Sectoring:
- Total cells (approx): 44
- Clusters (N=7): ≈ 6.3 → ~7 clusters
- Available channels = 10  
- Channels per cell = 10 / 7 ≈ 1.43  
- **Each cell gets ≈ 1 channel**

#### After Sectoring (3 Sectors per Cell):
- Channels per **cell sector** = 1.43 / 3 ≈ 0.48 → round to **1 per sector**, using reuse
- But sectoring allows reusing **the same channel in all 3 sectors** (due to isolation)

🔹 **Effective gain**: Up to **3× capacity**  
→ Now, **each cell effectively handles 3× the traffic** with the same spectrum.

---

### ✅ Does This Meet the Traffic Requirement?

Recall:
- **Total traffic in Z2** = 75 Erlangs
- For **2% blocking**, ~90 channels needed (from Erlang B)
- Available channels = 10 only → Clearly insufficient without sectoring

#### After Sectoring:
- Let’s say sectoring boosts each cell from handling 1.4 channels to effectively **~4.2 channels**
- Across 44 cells → Effective capacity ≈ **44 × 4.2 = 184.8 "virtual" channels**

✅ **Result**: This **exceeds** the 90-channel requirement → **Requirement met!**

---

### 📊 Updated Summary of Channel Capacity per Zone

| Zone | Reuse (N) | Sectoring | Channels Available | Effective Channels/Cell | Sufficient for Traffic? |
|------|-----------|-----------|--------------------|--------------------------|--------------------------|
| Z1   | 4         | No        | 10                 | ≈ 2.5                    | ❌ Needs dynamic/borrowing |
| Z2   | 7         | ✅ 3-sector | 10                 | ≈ 4.2 (via reuse)        | ✅ Yes (meets 75E)       |
| Z3   | 7         | No        | 10                 | ≈ 1.4                    | ✅ (low demand: 25E)      |

---

---

### **Step 9: Dynamic Allocation & Borrowing**

- **Z2** has the highest traffic. Borrow channels from **Z3** during peak hours.
- Z2 should use **cell sectoring** (3×120° antennas) to **triple its capacity** with the same frequencies.
- **Z1** can rely on **dynamic channel allocation** and limited borrowing from Z2.
- **Z3** is stable and doesn't need dynamic action due to lower demand.

---

### **Step 10: Technology Strategy by Zone**

| Zone | Primary Access Tech | Backup |
|------|----------------------|--------|
| Z1   | GSM + EDGE           | 3G     |
| Z2   | GSM + EDGE + Sectoring | 3G   |
| Z3   | Basic GSM (2G)       | 2G     |

---

## ✅ Final Summary

The reuse strategy ensures:
- **Efficient use of just 10 channels** by applying reuse factors (N=4 or 7)
- **Dynamic allocation and borrowing** to prevent congestion
- **Minimal co-channel interference**, especially in Z2 and Z3
- **High Grade of Service (GoS)** within acceptable 2% blocking limit
- **Technology mapping** ensures scalability and cost-efficiency


- **Zone 2’s sectoring** transforms its capacity, meeting the high traffic load with just 10 channels.
- **Zone 1** still requires **dynamic allocation and occasional borrowing** due to its density.
- **Zone 3** handles demand well, remaining stable with no sectoring.

This revised plan ensures:
- **Efficient utilization of all 10 channels**
- **Traffic demand is met** across all zones
- **High QoS** with ≤2% call blocking
- **Scalable and interference-minimized design**
