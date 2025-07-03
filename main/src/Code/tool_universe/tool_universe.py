"""from test.test_tool_drug_ingredients import run_tool_demo as run_tool_1
from test.test_tool_Adverse_Reactions import run_tool_demo as run_tool_2
from test.test_tool_Warnings import run_tool_demo as run_tool_3
from test.test_tool_Dosage_and_Storage import run_tool_demo as run_tool_4

if __name__ == "__main__":
    print("==== Running tool test for active ingredient info ====\n")
    run_tool_1()

    print("\n==== Running tool test for adverse reactions (side effects) ====\n")
    run_tool_2()

    print("\n==== Running tool test for warnings ====\n")
    run_tool_3()

    print("\n==== Running tool test for dosage and storage instructions ====\n")
    run_tool_4()"""

#%%
# main.py

# IMPORTANT:
# 1. Create a directory named 'test' in the same location as this main.py file.
# 2. Save all the 'test_tool_*.py' files provided into the 'test' directory.
# 3. Ensure 'tooluniverse' is installed in your Python environment (`pip install tooluniverse`).
# 4. Run this script from its parent directory: `python main.py`.
from test.test_tool_OpenTargets_get_drug_withdrawn_blackbox_status_by_chemblId import run_tool_demo as run_tool_11
from test.test_tool_OpenTargets_search_category_counts_by_query_string import run_tool_demo as run_tool_12
from test.test_tool_OpenTargets_get_disease_id_description_by_name import run_tool_demo as run_tool_13
from test.test_tool_OpenTargets_get_drug_id_description_by_name import run_tool_demo as run_tool_14
from test.test_tool_OpenTargets_get_drug_chembId_by_generic_name import run_tool_demo as run_tool_15
from test.test_tool_OpenTargets_get_drug_indications_by_chemblId import run_tool_demo as run_tool_16
from test.test_tool_OpenTargets_get_target_gene_ontology_by_ensemblID import run_tool_demo as run_tool_17
from test.test_tool_OpenTargets_get_target_homologues_by_ensemblID import run_tool_demo as run_tool_18
from test.test_tool_OpenTargets_get_target_safety_profile_by_ensemblID import run_tool_demo as run_tool_19
from test.test_tool_OpenTargets_get_biological_mouse_models_by_ensemblID import run_tool_demo as run_tool_20

from test.test_tool_OpenTargets_get_associated_targets_by_disease_efoId import run_tool_demo as run_tool_1
from test.test_tool_OpenTargets_get_diseases_phenotypes_by_target_ensembl import run_tool_demo as run_tool_2
from test.test_tool_OpenTargets_target_disease_evidence import run_tool_demo as run_tool_3
from test.test_tool_OpenTargets_get_drug_warnings_by_chemblId import run_tool_demo as run_tool_4
from test.test_tool_OpenTargets_get_drug_mechanisms_of_action_by_chemblId import run_tool_demo as run_tool_5
from test.test_tool_OpenTargets_get_associated_drugs_by_disease_efoId import run_tool_demo as run_tool_6
from test.test_tool_OpenTargets_get_similar_entities_by_disease_efoId import run_tool_demo as run_tool_7
from test.test_tool_OpenTargets_get_similar_entities_by_drug_chemblId import run_tool_demo as run_tool_8
from test.test_tool_OpenTargets_get_similar_entities_by_target_ensemblID import run_tool_demo as run_tool_9
from test.test_tool_OpenTargets_get_associated_phenotypes_by_disease_efoId import run_tool_demo as run_tool_10

from test.test_tool_OT_get_target_genomic_location_by_ensemblID import run_tool_demo as run_tool_21
from test.test_tool_OT_get_target_subcellular_locations_by_ensemblID import run_tool_demo as run_tool_22
from test.test_tool_OT_get_target_synonyms_by_ensemblID import run_tool_demo as run_tool_23
from test.test_tool_OT_get_target_tractability_by_ensemblID import run_tool_demo as run_tool_24
from test.test_tool_OT_get_target_classes_by_ensemblID import run_tool_demo as run_tool_25
from test.test_tool_OT_get_target_enabling_packages_by_ensemblID import run_tool_demo as run_tool_26
from test.test_tool_OT_get_target_interactions_by_ensemblID import run_tool_demo as run_tool_27
from test.test_tool_OT_get_disease_ancestors_parents_by_efoId import run_tool_demo as run_tool_28
from test.test_tool_OT_get_disease_descendants_children_by_efoId import run_tool_demo as run_tool_29
from test.test_tool_OT_get_disease_locations_by_efoId import run_tool_demo as run_tool_30

from test.test_tool_OT_get_disease_synonyms_by_efoId import run_tool_demo as run_tool_31
from test.test_tool_OT_get_disease_description_by_efoId import run_tool_demo as run_tool_32
from test.test_tool_OT_get_disease_therapeutic_areas_by_efoId import run_tool_demo as run_tool_33
from test.test_tool_OT_get_drug_adverse_events_by_chemblId import run_tool_demo as run_tool_34
from test.test_tool_OT_get_known_drugs_by_drug_chemblId import run_tool_demo as run_tool_35
from test.test_tool_OT_get_parent_child_molecules_by_drug_chembl_ID import run_tool_demo as run_tool_36
from test.test_tool_OT_get_approved_indications_by_drug_chemblId import run_tool_demo as run_tool_37
#from test.test_tool_OT_get_drug_description_by_chemblId import run_tool_demo as run_tool_38
from test.test_tool_OT_get_drug_synonyms_by_chemblId import run_tool_demo as run_tool_39
from test.test_tool_OT_get_drug_trade_names_by_chemblId import run_tool_demo as run_tool_40

from test.test_tool_OT_get_drug_approval_status_by_chemblId import run_tool_demo as run_tool_41
from test.test_tool_OT_get_chemical_probes_by_target_ensemblID import run_tool_demo as run_tool_42
from test.test_tool_OT_drug_pharmacogenomics_data import run_tool_demo as run_tool_43
from test.test_tool_OT_get_associated_drugs_by_target_ensemblID import run_tool_demo as run_tool_44
from test.test_tool_OT_get_associated_diseases_by_drug_chemblId import run_tool_demo as run_tool_45
from test.test_tool_OT_get_associated_targets_by_drug_chemblId import run_tool_demo as run_tool_46
from test.test_tool_OT_multi_entity_search_by_query_string import run_tool_demo as run_tool_47
from test.test_tool_OT_get_gene_ontology_terms_by_goID import run_tool_demo as run_tool_48
from test.test_tool_OT_get_target_constraint_info_by_ensemblID import run_tool_demo as run_tool_49
from test.test_tool_OT_get_publications_by_disease_efoId import run_tool_demo as run_tool_50

from test.test_tool_OT_get_publications_by_target_ensemblID import run_tool_demo as run_tool_51
from test.test_tool_OT_get_publications_by_drug_chemblId import run_tool_demo as run_tool_52
from test.test_tool_OT_get_target_id_description_by_name import run_tool_demo as run_tool_53
from test.test_tool_FDA_get_active_ingredient_info_by_drug_name import run_tool_demo as run_tool_54
from test.test_tool_FDA_get_dosage_and_storage_information_by_drug_name import run_tool_demo as run_tool_55
from test.test_tool_FDA_get_drug_names_by_abuse_info import run_tool_demo as run_tool_56
from test.test_tool_FDA_get_abuse_info_by_drug_name import run_tool_demo as run_tool_57
from test.test_tool_FDA_get_drug_names_by_accessories import run_tool_demo as run_tool_58
from test.test_tool_FDA_get_accessories_info_by_drug_name import run_tool_demo as run_tool_59
from test.test_tool_FDA_get_drug_names_by_active_ingredient import run_tool_demo as run_tool_60

from test.test_tool_FDA_get_manufacturer_name_NDC_number_by_drug_name import run_tool_demo as run_tool_61
from test.test_tool_FDA_get_drug_names_by_application_number_NDC_number import run_tool_demo as run_tool_62
from test.test_tool_FDA_get_drug_name_by_adverse_reaction import run_tool_demo as run_tool_63
from test.test_tool_FDA_get_adverse_reactions_by_drug_name import run_tool_demo as run_tool_64
from test.test_tool_FDA_get_drug_names_by_alarm import run_tool_demo as run_tool_65
from test.test_tool_FDA_get_alarms_by_drug_name import run_tool_demo as run_tool_66
from test.test_tool_FDA_get_drug_names_by_animal_pharmacology_info import run_tool_demo as run_tool_67
from test.test_tool_FDA_get_animal_pharmacology_info_by_drug_name import run_tool_demo as run_tool_68
from test.test_tool_FDA_get_drug_name_by_info_on_conditions_for_doctor_consultation import run_tool_demo as run_tool_69
from test.test_tool_FDA_get_info_on_conditions_for_doctor_consultation_by_drug_name import run_tool_demo as run_tool_70

from test.test_tool_FDA_get_drug_names_by_consulting_doctor_pharmacist_info import run_tool_demo as run_tool_71
from test.test_tool_FDA_get_info_on_consulting_doctor_pharmacist_by_drug_name import run_tool_demo as run_tool_72
from test.test_tool_FDA_get_drug_names_by_assembly_installation_info import run_tool_demo as run_tool_73
from test.test_tool_FDA_get_assembly_installation_info_by_drug_name import run_tool_demo as run_tool_74
from test.test_tool_FDA_get_drug_names_by_boxed_warning import run_tool_demo as run_tool_75
from test.test_tool_FDA_get_boxed_warning_info_by_drug_name import run_tool_demo as run_tool_76
from test.test_tool_FDA_get_drug_name_by_calibration_instructions import run_tool_demo as run_tool_77
from test.test_tool_FDA_get_calibration_instructions_by_drug_name import run_tool_demo as run_tool_78
from test.test_tool_FDA_get_drugs_by_carcinogenic_mutagenic_fertility import run_tool_demo as run_tool_79
from test.test_tool_FDA_get_carcinogenic_mutagenic_fertility_by_drug_name import run_tool_demo as run_tool_80

from test.test_tool_FDA_get_drug_name_by_SPL_ID import run_tool_demo as run_tool_81
from test.test_tool_FDA_get_drug_names_by_clinical_pharmacology import run_tool_demo as run_tool_82
from test.test_tool_FDA_get_clinical_pharmacology_by_drug_name import run_tool_demo as run_tool_83
from test.test_tool_FDA_get_drug_names_by_clinical_studies import run_tool_demo as run_tool_84
from test.test_tool_FDA_get_clinical_studies_info_by_drug_name import run_tool_demo as run_tool_85
from test.test_tool_FDA_get_drug_names_by_contraindications import run_tool_demo as run_tool_86
from test.test_tool_FDA_get_contraindications_by_drug_name import run_tool_demo as run_tool_87
from test.test_tool_FDA_get_drug_names_by_controlled_substance_DEA_schedule import run_tool_demo as run_tool_88
from test.test_tool_FDA_get_controlled_substance_DEA_schedule_info_by_drug_name import run_tool_demo as run_tool_89
from test.test_tool_FDA_get_drug_name_by_dependence_info import run_tool_demo as run_tool_90

from test.test_tool_FDA_get_dependence_info_by_drug_name import run_tool_demo as run_tool_91
from test.test_tool_FDA_get_drug_names_by_disposal_info import run_tool_demo as run_tool_92
from test.test_tool_FDA_get_disposal_info_by_drug_name import run_tool_demo as run_tool_93
from test.test_tool_FDA_get_drug_name_by_dosage_info import run_tool_demo as run_tool_94
from test.test_tool_FDA_get_drug_names_by_dosage_forms_and_strengths_info import run_tool_demo as run_tool_95
from test.test_tool_FDA_get_dosage_forms_and_strengths_by_drug_name import run_tool_demo as run_tool_96
from test.test_tool_FDA_get_drug_names_by_abuse_dependence_info import run_tool_demo as run_tool_97
from test.test_tool_FDA_get_abuse_dependence_info_by_drug_name import run_tool_demo as run_tool_98
from test.test_tool_FDA_get_drug_names_by_lab_test_interference import run_tool_demo as run_tool_99
from test.test_tool_FDA_get_lab_test_interference_info_by_drug_name import run_tool_demo as run_tool_100

from test.test_tool_FDA_get_drug_names_by_drug_interactions import run_tool_demo as run_tool_101
from test.test_tool_FDA_get_drug_interactions_by_drug_name import run_tool_demo as run_tool_102
from test.test_tool_FDA_get_drug_names_by_effective_time import run_tool_demo as run_tool_103
from test.test_tool_FDA_get_effective_time_by_drug_name import run_tool_demo as run_tool_104
from test.test_tool_FDA_get_drug_name_by_environmental_warning import run_tool_demo as run_tool_105
from test.test_tool_FDA_get_environmental_warning_by_drug_name import run_tool_demo as run_tool_106
from test.test_tool_FDA_get_drug_names_by_food_safety_warnings import run_tool_demo as run_tool_107
from test.test_tool_FDA_get_drug_names_by_general_precautions import run_tool_demo as run_tool_108
from test.test_tool_FDA_get_general_precautions_by_drug_name import run_tool_demo as run_tool_109
from test.test_tool_FDA_get_drug_names_by_geriatric_use import run_tool_demo as run_tool_110

if __name__ == "__main__":
    print("==== Running tool test for OpenTargets_get_associated_targets_by_disease_efoId ====\n")
    run_tool_1()

    print("\n==== Running tool test for OpenTargets_get_diseases_phenotypes_by_target_ensembl ====\n")
    run_tool_2()

    print("\n==== Running tool test for OpenTargets_target_disease_evidence ====\n")
    run_tool_3()

    print("\n==== Running tool test for OpenTargets_get_drug_warnings_by_chemblId ====\n")
    run_tool_4()

    print("\n==== Running tool test for OpenTargets_get_drug_mechanisms_of_action_by_chemblId ====\n")
    run_tool_5()

    print("\n==== Running tool test for OpenTargets_get_associated_drugs_by_disease_efoId ====\n")
    run_tool_6()

    print("\n==== Running tool test for OpenTargets_get_similar_entities_by_disease_efoId ====\n")
    run_tool_7()

    print("\n==== Running tool test for OpenTargets_get_similar_entities_by_drug_chemblId ====\n")
    run_tool_8()

    print("\n==== Running tool test for OpenTargets_get_similar_entities_by_target_ensemblID ====\n")
    run_tool_9()

    print("\n==== Running tool test for OpenTargets_get_associated_phenotypes_by_disease_efoId ====\n")
    run_tool_10()

        # Current batch calls
    print("\n==== Running tool test for OpenTargets_get_drug_withdrawn_blackbox_status_by_chemblId ====\n")
    run_tool_11()

    print("\n==== Running tool test for OpenTargets_search_category_counts_by_query_string ====\n")
    run_tool_12()

    print("\n==== Running tool test for OpenTargets_get_disease_id_description_by_name ====\n")
    run_tool_13()

    print("\n==== Running tool test for OpenTargets_get_drug_id_description_by_name ====\n")
    run_tool_14()

    print("\n==== Running tool test for OpenTargets_get_drug_chembId_by_generic_name ====\n")
    run_tool_15()

    print("\n==== Running tool test for OpenTargets_get_drug_indications_by_chemblId ====\n")
    run_tool_16()

    print("\n==== Running tool test for OpenTargets_get_target_gene_ontology_by_ensemblID ====\n")
    run_tool_17()

    print("\n==== Running tool test for OpenTargets_get_target_homologues_by_ensemblID ====\n")
    run_tool_18()

    print("\n==== Running tool test for OpenTargets_get_target_safety_profile_by_ensemblID ====\n")
    run_tool_19()

    print("\n==== Running tool test for OpenTargets_get_biological_mouse_models_by_ensemblID ====\n")
    run_tool_20()

    print("\n==== Running tool test for OpenTargets_get_target_genomic_location_by_ensemblID ====\n")
    run_tool_21()

    print("\n==== Running tool test for OpenTargets_get_target_subcellular_locations_by_ensemblID ====\n")
    run_tool_22()

    print("\n==== Running tool test for OpenTargets_get_target_synonyms_by_ensemblID ====\n")
    run_tool_23()

    print("\n==== Running tool test for OpenTargets_get_target_tractability_by_ensemblID ====\n")
    run_tool_24()

    print("\n==== Running tool test for OpenTargets_get_target_classes_by_ensemblID ====\n")
    run_tool_25()

    print("\n==== Running tool test for OpenTargets_get_target_enabling_packages_by_ensemblID ====\n")
    run_tool_26()

    print("\n==== Running tool test for OpenTargets_get_target_interactions_by_ensemblID ====\n")
    run_tool_27()

    print("\n==== Running tool test for OpenTargets_get_disease_ancestors_parents_by_efoId ====\n")
    run_tool_28()

    print("\n==== Running tool test for OpenTargets_get_disease_descendants_children_by_efoId ====\n")
    run_tool_29()

    print("\n==== Running tool test for OpenTargets_get_disease_locations_by_efoId ====\n")
    run_tool_30()


    # --- Current batch calls (newly generated) ---
    print("\n==== Running tool test for OpenTargets_get_disease_synonyms_by_efoId ====\n")
    run_tool_31()

    print("\n==== Running tool test for OpenTargets_get_disease_description_by_efoId ====\n")
    run_tool_32()

    print("\n==== Running tool test for OpenTargets_get_disease_therapeutic_areas_by_efoId ====\n")
    run_tool_33()

    print("\n==== Running tool test for OpenTargets_get_drug_adverse_events_by_chemblId ====\n")
    run_tool_34()

    print("\n==== Running tool test for OpenTargets_get_known_drugs_by_drug_chemblId ====\n")
    run_tool_35()

    print("\n==== Running tool test for OpenTargets_get_parent_child_molecules_by_drug_chembl_ID ====\n")
    run_tool_36()

    print("\n==== Running tool test for OpenTargets_get_approved_indications_by_drug_chemblId ====\n")
    run_tool_37()

    print("\n==== Running tool test for OpenTargets_get_drug_description_by_chemblId ====\n")
    #run_tool_38()

    print("\n==== Running tool test for OpenTargets_get_drug_synonyms_by_chemblId ====\n")
    run_tool_39()

    print("\n==== Running tool test for OpenTargets_get_drug_trade_names_by_chemblId ====\n")
    run_tool_40()


    # --- Current batch calls (newly generated) ---
    print("\n==== Running tool test for OpenTargets_get_drug_approval_status_by_chemblId ====\n")
    run_tool_41()

    print("\n==== Running tool test for OpenTargets_get_chemical_probes_by_target_ensemblID ====\n")
    run_tool_42()

    print("\n==== Running tool test for OpenTargets_drug_pharmacogenomics_data ====\n")
    run_tool_43()

    print("\n==== Running tool test for OpenTargets_get_associated_drugs_by_target_ensemblID ====\n")
    run_tool_44()

    print("\n==== Running tool test for OpenTargets_get_associated_diseases_by_drug_chemblId ====\n")
    run_tool_45()

    print("\n==== Running tool test for OpenTargets_get_associated_targets_by_drug_chemblId ====\n")
    run_tool_46()

    print("\n==== Running tool test for OpenTargets_multi_entity_search_by_query_string ====\n")
    run_tool_47()

    print("\n==== Running tool test for OpenTargets_get_gene_ontology_terms_by_goID ====\n")
    run_tool_48()

    print("\n==== Running tool test for OpenTargets_get_target_constraint_info_by_ensemblID ====\n")
    run_tool_49()

    print("\n==== Running tool test for OpenTargets_get_publications_by_disease_efoId ====\n")
    run_tool_50()

    print("\n==== Running tool test for OpenTargets_get_publications_by_target_ensemblID ====\n")
    run_tool_51()

    print("\n==== Running tool test for OpenTargets_get_publications_by_drug_chemblId ====\n")
    run_tool_52()

    print("\n==== Running tool test for OpenTargets_get_target_id_description_by_name ====\n")
    run_tool_53()

    print("\n==== Running tool test for FDA_get_active_ingredient_info_by_drug_name ====\n")
    run_tool_54()

    print("\n==== Running tool test for FDA_get_dosage_and_storage_information_by_drug_name ====\n")
    run_tool_55()

    print("\n==== Running tool test for FDA_get_drug_names_by_abuse_info ====\n")
    run_tool_56()

    print("\n==== Running tool test for FDA_get_abuse_info_by_drug_name ====\n")
    run_tool_57()

    print("\n==== Running tool test for FDA_get_drug_names_by_accessories ====\n")
    run_tool_58()

    print("\n==== Running tool test for FDA_get_accessories_info_by_drug_name ====\n")
    run_tool_59()

    print("\n==== Running tool test for FDA_get_drug_names_by_active_ingredient ====\n")
    run_tool_60()

    print("\n==== Running tool test for FDA_get_manufacturer_name_NDC_number_by_drug_name ====\n")
    run_tool_61()

    print("\n==== Running tool test for FDA_get_drug_names_by_application_number_NDC_number ====\n")
    run_tool_62()

    print("\n==== Running tool test for FDA_get_drug_name_by_adverse_reaction ====\n")
    run_tool_63()

    print("\n==== Running tool test for FDA_get_adverse_reactions_by_drug_name ====\n")
    run_tool_64()

    print("\n==== Running tool test for FDA_get_drug_names_by_alarm ====\n")
    run_tool_65()

    print("\n==== Running tool test for FDA_get_alarms_by_drug_name ====\n")
    run_tool_66()

    print("\n==== Running tool test for FDA_get_drug_names_by_animal_pharmacology_info ====\n")
    run_tool_67()

    print("\n==== Running tool test for FDA_get_animal_pharmacology_info_by_drug_name ====\n")
    run_tool_68()

    print("\n==== Running tool test for FDA_get_drug_name_by_info_on_conditions_for_doctor_consultation ====\n")
    run_tool_69()

    print("\n==== Running tool test for FDA_get_info_on_conditions_for_doctor_consultation_by_drug_name ====\n")
    run_tool_70()

    # --- Current new batch calls ---
    print("\n==== Running tool test for FDA_get_drug_names_by_consulting_doctor_pharmacist_info ====\n")
    run_tool_71()

    print("\n==== Running tool test for FDA_get_info_on_consulting_doctor_pharmacist_by_drug_name ====\n")
    run_tool_72()

    print("\n==== Running tool test for FDA_get_drug_names_by_assembly_installation_info ====\n")
    run_tool_73()

    print("\n==== Running tool test for FDA_get_assembly_installation_info_by_drug_name ====\n")
    run_tool_74()

    print("\n==== Running tool test for FDA_get_drug_names_by_boxed_warning ====\n")
    run_tool_75()

    print("\n==== Running tool test for FDA_get_boxed_warning_info_by_drug_name ====\n")
    run_tool_76()

    print("\n==== Running tool test for FDA_get_drug_name_by_calibration_instructions ====\n")
    run_tool_77()

    print("\n==== Running tool test for FDA_get_calibration_instructions_by_drug_name ====\n")
    run_tool_78()

    print("\n==== Running tool test for FDA_get_drugs_by_carcinogenic_mutagenic_fertility ====\n")
    run_tool_79()

    print("\n==== Running tool test for FDA_get_carcinogenic_mutagenic_fertility_by_drug_name ====\n")
    run_tool_80()

    print("\n==== Running tool test for FDA_get_drug_name_by_SPL_ID ====\n")
    run_tool_81()

    print("\n==== Running tool test for FDA_get_drug_names_by_clinical_pharmacology ====\n")
    run_tool_82()

    print("\n==== Running tool test for FDA_get_clinical_pharmacology_by_drug_name ====\n")
    run_tool_83()

    print("\n==== Running tool test for FDA_get_drug_names_by_clinical_studies ====\n")
    run_tool_84()

    print("\n==== Running tool test for FDA_get_clinical_studies_info_by_drug_name ====\n")
    run_tool_85()

    print("\n==== Running tool test for FDA_get_drug_names_by_contraindications ====\n")
    run_tool_86()

    print("\n==== Running tool test for FDA_get_contraindications_by_drug_name ====\n")
    run_tool_87()

    print("\n==== Running tool test for FDA_get_drug_names_by_controlled_substance_DEA_schedule ====\n")
    run_tool_88()

    print("\n==== Running tool test for FDA_get_controlled_substance_DEA_schedule_info_by_drug_name ====\n")
    run_tool_89()

    print("\n==== Running tool test for FDA_get_drug_name_by_dependence_info ====\n")
    run_tool_90()


    # --- Current new batch calls (starting from run_tool_91) ---
    print("\n==== Running tool test for FDA_get_dependence_info_by_drug_name ====\n")
    run_tool_91()

    print("\n==== Running tool test for FDA_get_drug_names_by_disposal_info ====\n")
    run_tool_92()

    print("\n==== Running tool test for FDA_get_disposal_info_by_drug_name ====\n")
    run_tool_93()

    print("\n==== Running tool test for FDA_get_drug_name_by_dosage_info ====\n")
    run_tool_94()

    print("\n==== Running tool test for FDA_get_drug_names_by_dosage_forms_and_strengths_info ====\n")
    run_tool_95()

    print("\n==== Running tool test for FDA_get_dosage_forms_and_strengths_by_drug_name ====\n")
    run_tool_96()

    print("\n==== Running tool test for FDA_get_drug_names_by_abuse_dependence_info ====\n")
    run_tool_97()

    print("\n==== Running tool test for FDA_get_abuse_dependence_info_by_drug_name ====\n")
    run_tool_98()

    print("\n==== Running tool test for FDA_get_drug_names_by_lab_test_interference ====\n")
    run_tool_99()

    print("\n==== Running tool test for FDA_get_lab_test_interference_info_by_drug_name ====\n")
    run_tool_100()

    print("\n==== Running tool test for FDA_get_drug_names_by_drug_interactions ====\n")
    run_tool_101()

    print("\n==== Running tool test for FDA_get_drug_interactions_by_drug_name ====\n")
    run_tool_102()

    print("\n==== Running tool test for FDA_get_drug_names_by_effective_time ====\n")
    run_tool_103()

    print("\n==== Running tool test for FDA_get_effective_time_by_drug_name ====\n")
    run_tool_104()

    print("\n==== Running tool test for FDA_get_drug_name_by_environmental_warning ====\n")
    run_tool_105()

    print("\n==== Running tool test for FDA_get_environmental_warning_by_drug_name ====\n")
    run_tool_106()

    print("\n==== Running tool test for FDA_get_drug_names_by_food_safety_warnings ====\n")
    run_tool_107()

    print("\n==== Running tool test for FDA_get_drug_names_by_general_precautions ====\n")
    run_tool_108()

    print("\n==== Running tool test for FDA_get_general_precautions_by_drug_name ====\n")
    run_tool_109()

    print("\n==== Running tool test for FDA_get_drug_names_by_geriatric_use ====\n")
    run_tool_110()

