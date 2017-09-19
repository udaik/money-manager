mongoose = require('mongoose')
schema = mongoose.Schema

class AccountSchema

  constructor:(db, type, name, balance, ifsc_code, acnt_number, interest_rate, mab)->
    @db = db
    @type = type
    @name = name
    @balance = balance
    @ifsc_code = ifsc_code
    @acnt_number = acnt_number
    @interest_rate = interest_rate
    @mab = @mab

    acnt_schema = new Schema({
      type :  String,
      name : String,
      balance : Number,

      date: {
        type: Date,
        default: Date.now
        },

      inst_details : {
        ifsc_code : String,
        acnt_number : String,
        inst_name : String
      }

      meta : {
        accessed : Number,
      }
    })
