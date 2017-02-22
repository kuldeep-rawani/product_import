from flask import Flask
import flask

class SeException(Exception):

    def __init__(self, statusCode, seCode, message, hint=None):
        self.message = message
        self.statusCode = statusCode
        self.seCode = seCode
        self.hint = hint
    ##
    # To Throw Custom SeException
    # @param self.statusCode string
    # @param se_code number
    # @param message string
    # @return response json
    ##
    def throw_se_exception(self):
        response = flask.jsonify({
            'code': self.statusCode,
            'data':[],
            'notification': {
                'hint':self.hint, 
                'message':self.message,
                'seCode': self.seCode, 
                'type':'error'
            }
        })
        response.status_code = self.statusCode
        return response 