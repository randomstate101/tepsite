from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



from django.utils.encoding import python_2_unicode_compatible





class Program(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return self.name
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')

)
ANSWER_CHOICES=(
     ('Strongly Disagree','Strongly Disagree'),
     ('Disagree','Disagree'),
     ('Neutral','Neutral'),
     ('Agree','Agree'),
     ('Strongly Agree', 'Strongly Agree'),
)


class ProgramFeedbackForm(models.Model):
    intern_name = models.CharField(max_length=30,blank=True,null=True)

    date_posted = models.DateTimeField(default=timezone.now)
    program = models.ForeignKey(Program,blank=True,null=True, on_delete= models.CASCADE)
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Overall_my_impression_of_this_course_was_excellent = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_course_objectives_were_clearly_stated_and_used_understandable_terms=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    This_course_met_the_defined_objectives = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Both_the_facility_and_equipment_used_met_all_needs_of_the_course = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_course_materials_were_both_useful_and_easy_to_follow  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_instructor_demonstrated_thorough_knowledge_and_understanding_of_the_topic = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_instructor_presented_information_in_a_clear_understandable_and_professional_manner= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_amount_of_time_scheduled_for_this_course_was_exactly_what_was_needed_to_meet_the_objectives= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    This_course_relates_directly_to_my_current_job_responsibilities = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_would_recommend_this_course_to_other_teammates  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    details = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.intern_name

class SixThinkingHats_SelfEvaluation(models.Model):

     intern_name = models.CharField(max_length=40)
     email = models.EmailField()
     I_try_to_formulate_a_clear_definition_of_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_goal_and_outcome_of_the_problem_I_am_facing = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_plan_to_figure_out_the_most_effective_method_to_proceed_from_the_initial_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_organize_and_arrange_my_thinking_to_help_move_me_beyond_my_present_circumstances = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_figure_out_what_I_know_about_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_figure_out_what_I_dont_know_about_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_how_I_will_go_about_acquiring_the_facts_stats_and_data_that_will_help_me_resolve_this_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_figure_out_potential_solutions_exist_based_on_the_facts_stats_and_data_I_have_collected  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_consider_what_my_feelings_tell_me_about_the_choice_I_am_about_to_make = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_better_ways_to_solve_a_problem_based_on_my_feelings = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_if_the_solution_is_the_right_one_based_on_my_intuition = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_find_fatal_flaws_in_a_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_consider_the_potential_risks_and_consequences_associated_with_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_if_I_have_the_necessary_resources_skills_and_support_to_solve_the_problem_or_not =  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_how_I_can_logically_and_realistically_make_the_solution_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_positive_outcomes_that_could_result_from_an_action = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_long_term_benefits_of_an_action= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_alternative_possibilities_that_could_exist_when_considering_a_decision = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_different_ways_I_could_approach_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_think_of_an_out_of_the_box_solution = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

     def __str__(self):
         return self.intern_name




class Six_hats_Writeup(models.Model):
    intern_name = models.CharField(max_length=40)
    email=models.EmailField()
    Write_a_brief_write_up_about_how_you_effectively_used_Six_Thinking_Hats_technique_to_solve_a_problem_at_the_workplace = models.TextField()

    def __str__(self):
        return self.intern_name


class Man_eff_SelfEvaluation(models.Model):
    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    I_identify_what_and_when_to_delegate_a_task_or_role_that_will_be_motivating_for_your_employees = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_give_constructive_behavior_based_feedback = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_practise_active_listening = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_assess_conflict_situations_and_apply_the_most_appropriate_modes = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_practice_overall_team_management_and_effective_leadership_skills = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_identify_when_is_the_best_time_to_tell_vs_ask_in_a_conversation = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_know_the_types_of_questions_to_use_to_dig_deeper_into_a_conversation = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name

class Man_eff_RelationshipWithManager(models.Model):

    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Name_of_your_Manager = models.CharField(max_length=50)
    My_manager_understands_my_problems_and_needs =  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_manager_recognizes_my_potential = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Regardless_of_how_much_power_he_she_has_built_into_his_her_position_my_manager_would_be_personally_inclined_to_use_his_her_power_to_help_me_solve_problems_in_my_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_supervisor_has_enough_confidence_in_me_that_he_she_would_defend_and_justify_my_decisions_if_I_were_not_present_to_do_so = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_can_count_on_my_manager_to_bail_me_out_at_his_her_expense_when_I_really_need_it = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_manager_has_enough_confidence_in_me_that_he_she_would_defend_and_justiy_my_decision_if_I_am_not_present_to_do_so = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_know_how_satisfied_my_manager_is_with_what_I_do = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name


class Man_eff_Employee_Engagement(models.Model):

    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Name_of_your_Manager = models.CharField(max_length=50)
    I_know_what_is_expected_of_me_at_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_willing_to_really_push_myself_to_reach_challenging_work_goals = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_have_the_opportunity_to_do_what_I_do_best_every_day = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_supervisor_or_someone_at_work_seems_to_care_about_my_personal_development = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_enthusiastic_about_providing_a_high_quality_product_or_service = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_always_willing_to_go_the_extra_mile_in_order_to_do_my_job_well = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Trying_to_constantly_improve_my_job_performance_is_very_important_to_me = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_job_is_a_source_of_personal_pride_for_me = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_receive_recognition_or_praise_for_doing_good_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_opinions_seem_to_count_at_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Someone_has_talked_to_me_about_my_progress_in_the_past_6_months = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name



















LEVEL_CHOICES = (
     ('warning', 'Warning'),
     ('error', 'Error'),
     ('success', 'Success'),
     ('info', 'Info'),
)

class Announcement(models.Model):
    """
    Model to hold global announcements
    """
    body = models.TextField(blank=False)
    display = models.BooleanField(default=False)
    level = models.CharField(max_length=7,
                choices=LEVEL_CHOICES, default='info')

    def __unicode__(self):
        return self.body[:50]
