import datetime as dt

APP_NAME = "NextCure Signal Room"
APP_VERSION = "v1.4 Backend-Ready Scaffold"
API_URL = "https://clinicaltrials.gov/api/v2/studies"
TODAY = dt.date.today()

TARGET_LANES = {
    "B7-H4 / VTCN1": ["B7-H4", "B7H4", "VTCN1", "B7 H4", "LNCB74", "B7-H4 ADC", "anti-B7-H4"],
    "CDH6": ["CDH6", "cadherin 6", "cadherin-6", "SIM0505", "CDH6 ADC", "anti-CDH6"],
    "Alzheimer's / ApoE4": ["Alzheimer", "Alzheimer's", "ApoE4", "APOE4", "APOE", "NC181"],
    "Bone / Siglec-15": ["osteogenesis imperfecta", "bone disease", "bone", "Siglec-15", "SIGLEC15", "NC605"],
}

PRESET_QUERIES = [
    "B7-H4 OR VTCN1 OR LNCB74 OR B7H4",
    "CDH6 OR cadherin 6 OR SIM0505",
    "Alzheimer ApoE4 OR APOE4 OR NC181",
    "Siglec-15 OR osteogenesis imperfecta OR NC605 bone",
]

PRESET_PAGE_SIZE = 100
ACTIVE_STATUSES = {"Recruiting", "Not yet recruiting", "Active, not recruiting", "Enrolling by invitation"}
PLANNED_STATUSES = {"Not yet recruiting"}
STATUS_FOCUS = ["Recruiting", "Not yet recruiting", "Active, not recruiting", "Enrolling by invitation"]

PHASE_ORDER = ["Early Phase 1", "Phase 1", "Phase 1/2", "Phase 2", "Phase 2/3", "Phase 3", "Phase 4", "Phase not listed"]
COMBO_TERMS = [
    "combination", "combined", "plus", "+", "with pembrolizumab", "pembrolizumab", "keytruda",
    "nivolumab", "opdivo", "atezolizumab", "durvalumab", "cemiplimab", "immunotherapy",
    "checkpoint", "PD-1", "PD-L1", "chemotherapy", "carboplatin", "paclitaxel", "gemcitabine",
    "bevacizumab", "olaparib", "niraparib", "targeted therapy"
]
