from jira import JIRA
import json
import operator

def define_input(prediction_df, username, password, number):

    auth_jira = JIRA(server='https://intelex.atlassian.net', auth=(username, password))
    issue = auth_jira.issue(number)

    print('Manual prediction was: `', issue.fields.customfield_10049, '`')

    for column in prediction_df.columns:
        if 'ML-' in column:
            prediction_df.loc[0, column] = 0
        for label in issue.fields.labels:
            if 'ML-' in label:
                prediction_df.loc[0, label] = 1
    print('Predicting points for `', issue.fields.summary, '` User Story.')
    print('With ' + str(issue.fields.labels) + ' labels ')

    return prediction_df

def one_hot_decode(coded):
    decoded = coded.dot([1, 2,3,5,8]).astype(int)

    try:
        decoded[:] = [1 if x == 0 else 8 if x > 8 else x for x in decoded]
    except TypeError:
        return 1 if decoded == 0 else 8 if decoded > 8 else decoded
    return decoded

def _fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return _fibonacci(n-1)+_fibonacci(n-2)

def predict_points(classifier, prediction_df):

    # try:
    estimator = classifier.best_estimator_.estimators_[0]
    result = {}
    predict = classifier.predict(prediction_df)
    if hasattr(estimator, 'predict_proba'):
        predict_prop = classifier.predict_proba(prediction_df)
        index, value = max(enumerate(predict_prop[0]), key=operator.itemgetter(1))
        predicted_point = _fibonacci(index+2)
        possibility = round(value,2)*100
        print('[',type(estimator).__name__, '] prediction is:',
              predicted_point, ' points with ', possibility,'% probability')
        result['prediction'] = str(predicted_point)
        result['probability'] = str(possibility)
        result['status'] = 'Ok'
        return result
        #return {"prediction": predicted_point, "probability":possibility, "status": "Ok"}
    else:
        prediction = one_hot_decode(predict)[0]
        print('[',type(estimator).__name__, '] prediction is: ', prediction, ' points')
        result['prediction'] = str(prediction)
        result['probability'] = "100"
        result['status'] = 'Ok'
        return result
        #return {"prediction": prediction, "probability":100, "status": "Ok"}
    # except Exception, e:
    #     return {"prediction": -1, "probability": -1, "status": str(e)}
    #     raise
