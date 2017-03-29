package za.co.cti;

import java.util.Vector;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MultiChoiceQuestionsActivity 
extends Activity
implements OnClickListener {
	private TextView question;
	private TextView summary;
	private Vector<MCQuestion> questions;
	private RadioGroup opts;
	private MCQuestion currentQuestion;
	private int noCorrect;
	private int noAnswered;
	private int noQuestions = 3;
	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.multichoice);
        Log.i("MCQ", "MultiChoice starts");
        opts = (RadioGroup) findViewById(R.id.opts);
        Button sub = (Button) findViewById(R.id.submit);
        question = (TextView) findViewById(R.id.question_text);
        summary = (TextView) findViewById(R.id.multichoice_summary);  
        noCorrect = 0;
        noAnswered = 0;
        sub.setOnClickListener(this);
        initialiseQuestions();
        generateSummary();
        generateQuestion(0);
    }

	private void generateQuestion(int noQ) {
		opts.removeAllViews();
		currentQuestion = questions.get(noQ);
		question.setText(currentQuestion.getQuestion());
		int i = 1;
		for( String ans: currentQuestion.getAnswers()) {
			RadioButton rb = new RadioButton(this);
			rb.setText(ans);
			rb.setId(i++);
			opts.addView(rb);
		}
	}

	private void initialiseQuestions() {
		questions = new Vector<MCQuestion>();
		MCQuestion q1 = new MCQuestion("What is the capital city of South Africa?");
		q1.addAnswer("Johannesburg", false);
		q1.addAnswer("Cape Town", false);
		q1.addAnswer("Pretoria", true);
		q1.addAnswer("Bloomfontein", false);
		questions.add(q1);	
		q1 = new MCQuestion("How many provinces does south africa has?");
		q1.addAnswer("4", false);
		q1.addAnswer("9", true);
		q1.addAnswer("11", false);
		questions.add(q1);	
		q1 = new MCQuestion("Where is the UK situated?");
		q1.addAnswer("Africa", false);
		q1.addAnswer("Europe", true);
		q1.addAnswer("Asia", false);
		q1.addAnswer("America", false);
		questions.add(q1);	
		// more questions could be added
		}
	
	   private void generateSummary()
	    {
	    	summary.setText( noCorrect + " answers out of " + noAnswered 
	    			+ " attempted of " +noQuestions + " questions");
	    }

	public void onClick(View arg0) {
		noAnswered++;
		int id;
		id = opts.getCheckedRadioButtonId();
		if( currentQuestion.isCorrect(id))
			noCorrect++;
		generateSummary();
		if (noAnswered == noQuestions)
			finish();
		else
			generateQuestion(noAnswered);
	}
}