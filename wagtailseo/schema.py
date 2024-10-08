SCHEMA_HELP = (
    "Structured data defines brand, contact, and storefront information to "
    "search engines. This information applies to the whole site."
    "If your organization has multiple locations or branches, also provide "
    "this info on each page representing the location."
)

# fmt: off
SCHEMA_ORG_CHOICES = (
    ("Organization", "Organization"),
    ("Airline", "Organization > Airline"),
    ("Corporation", "Organization > Corporation"),
    ("EducationalOrganization", "Organization > EducationalOrganization"),
    ("CollegeOrUniversity", "Organization > EducationalOrganization > CollegeOrUniversity"),
    ("ElementarySchool", "Organization > EducationalOrganization > ElementarySchool"),
    ("HighSchool", "Organization > EducationalOrganization > HighSchool"),
    ("MiddleSchool", "Organization > EducationalOrganization > MiddleSchool"),
    ("Preschool", "Organization > EducationalOrganization > Preschool"),
    ("School", "Organization > EducationalOrganization > School"),
    ("GovernmentOrganization", "Organization > GovernmentOrganization"),
    ("LocalBusiness", "Organization > LocalBusiness"),
    ("AnimalShelter", "Organization > LocalBusiness > AnimalShelter"),
    ("AutomotiveBusiness", "Organization > LocalBusiness > AutomotiveBusiness"),
    ("AutoBodyShop", "Organization > LocalBusiness > AutomotiveBusiness > AutoBodyShop"),
    ("AutoDealer", "Organization > LocalBusiness > AutomotiveBusiness > AutoDealer"),
    ("AutoPartsStore", "Organization > LocalBusiness > AutomotiveBusiness > AutoPartsStore"),
    ("AutoRental", "Organization > LocalBusiness > AutomotiveBusiness > AutoRental"),
    ("AutoRepair", "Organization > LocalBusiness > AutomotiveBusiness > AutoRepair"),
    ("AutoWash", "Organization > LocalBusiness > AutomotiveBusiness > AutoWash"),
    ("GasStation", "Organization > LocalBusiness > AutomotiveBusiness > GasStation"),
    ("MotorcycleDealer", "Organization > LocalBusiness > AutomotiveBusiness > MotorcycleDealer"),
    ("MotorcycleRepair", "Organization > LocalBusiness > AutomotiveBusiness > MotorcycleRepair"),
    ("ChildCare", "Organization > LocalBusiness > ChildCare"),
    ("Dentist", "Organization > LocalBusiness > Dentist"),
    ("DryCleaningOrLaundry", "Organization > LocalBusiness > DryCleaningOrLaundry"),
    ("EmergencyService", "Organization > LocalBusiness > EmergencyService"),
    ("FireStation", "Organization > LocalBusiness > EmergencyService > FireStation"),
    ("Hospital", "Organization > LocalBusiness > EmergencyService > Hospital"),
    ("PoliceStation", "Organization > LocalBusiness > EmergencyService > PoliceStation"),
    ("EmploymentAgency", "Organization > LocalBusiness > EmploymentAgency"),
    ("EntertainmentBusiness", "Organization > LocalBusiness > EntertainmentBusiness"),
    ("AdultEntertainment", "Organization > LocalBusiness > EntertainmentBusiness > AdultEntertainment"),
    ("AmusementPark", "Organization > LocalBusiness > EntertainmentBusiness > AmusementPark"),
    ("ArtGallery", "Organization > LocalBusiness > EntertainmentBusiness > ArtGallery"),
    ("Casino", "Organization > LocalBusiness > EntertainmentBusiness > Casino"),
    ("ComedyClub", "Organization > LocalBusiness > EntertainmentBusiness > ComedyClub"),
    ("MovieTheater", "Organization > LocalBusiness > EntertainmentBusiness > MovieTheater"),
    ("NightClub", "Organization > LocalBusiness > EntertainmentBusiness > NightClub"),
    ("FinancialService", "Organization > LocalBusiness > FinancialService"),
    ("AccountingService", "Organization > LocalBusiness > FinancialService > AccountingService"),
    ("AutomatedTeller", "Organization > LocalBusiness > FinancialService > AutomatedTeller"),
    ("BankOrCreditUnion", "Organization > LocalBusiness > FinancialService > BankOrCreditUnion"),
    ("InsuranceAgency", "Organization > LocalBusiness > FinancialService > InsuranceAgency"),
    ("FoodEstablishment", "Organization > LocalBusiness > FoodEstablishment"),
    ("Bakery", "Organization > LocalBusiness > FoodEstablishment > Bakery"),
    ("BarOrPub", "Organization > LocalBusiness > FoodEstablishment > BarOrPub"),
    ("Brewery", "Organization > LocalBusiness > FoodEstablishment > Brewery"),
    ("CafeOrCoffeeShop", "Organization > LocalBusiness > FoodEstablishment > CafeOrCoffeeShop"),
    ("FastFoodRestaurant", "Organization > LocalBusiness > FoodEstablishment > FastFoodRestaurant"),
    ("IceCreamShop", "Organization > LocalBusiness > FoodEstablishment > IceCreamShop"),
    ("Restaurant", "Organization > LocalBusiness > FoodEstablishment > Restaurant"),
    ("Winery", "Organization > LocalBusiness > FoodEstablishment > Winery"),
    ("GovernmentOffice", "Organization > LocalBusiness > GovernmentOffice"),
    ("PostOffice", "Organization > LocalBusiness > GovernmentOffice > PostOffice"),
    ("HealthAndBeautyBusiness", "Organization > LocalBusiness > HealthAndBeautyBusiness"),
    ("BeautySalon", "Organization > LocalBusiness > HealthAndBeautyBusiness > BeautySalon"),
    ("DaySpa", "Organization > LocalBusiness > HealthAndBeautyBusiness > DaySpa"),
    ("HairSalon", "Organization > LocalBusiness > HealthAndBeautyBusiness > HairSalon"),
    ("HealthClub", "Organization > LocalBusiness > HealthAndBeautyBusiness > HealthClub"),
    ("NailSalon", "Organization > LocalBusiness > HealthAndBeautyBusiness > NailSalon"),
    ("TattooParlor", "Organization > LocalBusiness > HealthAndBeautyBusiness > TattooParlor"),
    ("HomeAndConstructionBusiness", "Organization > LocalBusiness > HomeAndConstructionBusiness"),
    ("Electrician", "Organization > LocalBusiness > HomeAndConstructionBusiness > Electrician"),
    ("GeneralContractor", "Organization > LocalBusiness > HomeAndConstructionBusiness > GeneralContractor"),
    ("HVACBusiness", "Organization > LocalBusiness > HomeAndConstructionBusiness > HVACBusiness"),
    ("HousePainter", "Organization > LocalBusiness > HomeAndConstructionBusiness > HousePainter"),
    ("Locksmith", "Organization > LocalBusiness > HomeAndConstructionBusiness > Locksmith"),
    ("MovingCompany", "Organization > LocalBusiness > HomeAndConstructionBusiness > MovingCompany"),
    ("Plumber", "Organization > LocalBusiness > HomeAndConstructionBusiness > Plumber"),
    ("RoofingContractor", "Organization > LocalBusiness > HomeAndConstructionBusiness > RoofingContractor"),
    ("InternetCafe", "Organization > LocalBusiness > InternetCafe"),
    ("LegalService", "Organization > LocalBusiness > LegalService"),
    ("Attorney", "Organization > LocalBusiness > LegalService > Attorney"),
    ("Notary", "Organization > LocalBusiness > LegalService > Notary"),
    ("Library", "Organization > LocalBusiness > Library"),
    ("LodgingBusiness", "Organization > LocalBusiness > LodgingBusiness"),
    ("BedAndBreakfast", "Organization > LocalBusiness > LodgingBusiness > BedAndBreakfast"),
    ("Campground", "Organization > LocalBusiness > LodgingBusiness > Campground"),
    ("Hostel", "Organization > LocalBusiness > LodgingBusiness > Hostel"),
    ("Hotel", "Organization > LocalBusiness > LodgingBusiness > Hotel"),
    ("Motel", "Organization > LocalBusiness > LodgingBusiness > Motel"),
    ("Resort", "Organization > LocalBusiness > LodgingBusiness > Resort"),
    ("ProfessionalService", "Organization > LocalBusiness > ProfessionalService"),
    ("RadioStation", "Organization > LocalBusiness > RadioStation"),
    ("RealEstateAgent", "Organization > LocalBusiness > RealEstateAgent"),
    ("RecyclingCenter", "Organization > LocalBusiness > RecyclingCenter"),
    ("SelfStorage", "Organization > LocalBusiness > SelfStorage"),
    ("ShoppingCenter", "Organization > LocalBusiness > ShoppingCenter"),
    ("SportsActivityLocation", "Organization > LocalBusiness > SportsActivityLocation"),
    ("BowlingAlley", "Organization > LocalBusiness > SportsActivityLocation > BowlingAlley"),
    ("ExerciseGym", "Organization > LocalBusiness > SportsActivityLocation > ExerciseGym"),
    ("GolfCourse", "Organization > LocalBusiness > SportsActivityLocation > GolfCourse"),
    ("HealthClub", "Organization > LocalBusiness > SportsActivityLocation > HealthClub"),
    ("PublicSwimmingPool", "Organization > LocalBusiness > SportsActivityLocation > PublicSwimmingPool"),
    ("SkiResort", "Organization > LocalBusiness > SportsActivityLocation > SkiResort"),
    ("SportsClub", "Organization > LocalBusiness > SportsActivityLocation > SportsClub"),
    ("StadiumOrArena", "Organization > LocalBusiness > SportsActivityLocation > StadiumOrArena"),
    ("TennisComplex", "Organization > LocalBusiness > SportsActivityLocation > TennisComplex"),
    ("Store", "Organization > LocalBusiness > Store"),
    ("AutoPartsStore", "Organization > LocalBusiness > Store > AutoPartsStore"),
    ("BikeStore", "Organization > LocalBusiness > Store > BikeStore"),
    ("BookStore", "Organization > LocalBusiness > Store > BookStore"),
    ("ClothingStore", "Organization > LocalBusiness > Store > ClothingStore"),
    ("ComputerStore", "Organization > LocalBusiness > Store > ComputerStore"),
    ("ConvenienceStore", "Organization > LocalBusiness > Store > ConvenienceStore"),
    ("DepartmentStore", "Organization > LocalBusiness > Store > DepartmentStore"),
    ("ElectronicsStore", "Organization > LocalBusiness > Store > ElectronicsStore"),
    ("Florist", "Organization > LocalBusiness > Store > Florist"),
    ("FurnitureStore", "Organization > LocalBusiness > Store > FurnitureStore"),
    ("GardenStore", "Organization > LocalBusiness > Store > GardenStore"),
    ("GroceryStore", "Organization > LocalBusiness > Store > GroceryStore"),
    ("HardwareStore", "Organization > LocalBusiness > Store > HardwareStore"),
    ("HobbyShop", "Organization > LocalBusiness > Store > HobbyShop"),
    ("HomeGoodsStore", "Organization > LocalBusiness > Store > HomeGoodsStore"),
    ("JewelryStore", "Organization > LocalBusiness > Store > JewelryStore"),
    ("LiquorStore", "Organization > LocalBusiness > Store > LiquorStore"),
    ("MensClothingStore", "Organization > LocalBusiness > Store > MensClothingStore"),
    ("MobilePhoneStore", "Organization > LocalBusiness > Store > MobilePhoneStore"),
    ("MovieRentalStore", "Organization > LocalBusiness > Store > MovieRentalStore"),
    ("MusicStore", "Organization > LocalBusiness > Store > MusicStore"),
    ("OfficeEquipmentStore", "Organization > LocalBusiness > Store > OfficeEquipmentStore"),
    ("OutletStore", "Organization > LocalBusiness > Store > OutletStore"),
    ("PawnShop", "Organization > LocalBusiness > Store > PawnShop"),
    ("PetStore", "Organization > LocalBusiness > Store > PetStore"),
    ("ShoeStore", "Organization > LocalBusiness > Store > ShoeStore"),
    ("SportingGoodsStore", "Organization > LocalBusiness > Store > SportingGoodsStore"),
    ("TireShop", "Organization > LocalBusiness > Store > TireShop"),
    ("ToyStore", "Organization > LocalBusiness > Store > ToyStore"),
    ("WholesaleStore", "Organization > LocalBusiness > Store > WholesaleStore"),
    ("TelevisionStation", "Organization > LocalBusiness > TelevisionStation"),
    ("TouristInformationCenter", "Organization > LocalBusiness > TouristInformationCenter"),
    ("TravelAgency", "Organization > LocalBusiness > TravelAgency"),
    ("MedicalOrganization", "Organization > MedicalOrganization"),
    ("Dentist", "Organization > MedicalOrganization > Dentist"),
    ("Hospital", "Organization > MedicalOrganization > Hospital"),
    ("Pharmacy", "Organization > MedicalOrganization > Pharmacy"),
    ("Physician", "Organization > MedicalOrganization > Physician"),
    ("NGO", "Organization > NGO"),
    ("PerformingGroup", "Organization > PerformingGroup"),
    ("DanceGroup", "Organization > PerformingGroup > DanceGroup"),
    ("MusicGroup", "Organization > PerformingGroup > MusicGroup"),
    ("TheaterGroup", "Organization > PerformingGroup > TheaterGroup"),
    ("SportsOrganization", "Organization > SportsOrganization"),
    ("SportsTeam", "Organization > SportsOrganization > SportsTeam"),
)

SCHEMA_ACTION_CHOICES = (
    ("OrderAction", "OrderAction"),
    ("ReserveAction", "ReserveAction"),
)

SCHEMA_RESULT_CHOICES = (
    ("Reservation", "Reservation"),
    ("BusReservation", "BusReservation"),
    ("EventReservation", "EventReservation"),
    ("FlightReservation", "FlightReservation"),
    ("FoodEstablishmentReservation", "FoodEstablishmentReservation"),
    ("LodgingReservation", "LodgingReservation"),
    ("RentalCarReservation", "RentalCarReservation"),
    ("ReservationPackage", "ReservationPackage"),
    ("TaxiReservation", "TaxiReservation"),
    ("TrainReservation", "TrainReservation"),
)
# fmt: on
