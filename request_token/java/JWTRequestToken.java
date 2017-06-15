package com.telesign.example.jwt;

import static org.apache.commons.codec.binary.Base64.encodeBase64URLSafeString;

import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.Mac;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Base64;
import org.json.JSONObject;

/***
 * 
 * Reference implementation to generate a valid TeleSign RequestToken. You can
 * use this lib (or a functionality equivalent one) to generate tokens and then
 * host them on whatever Java Web Services framework you like.
 * 
 * NOTE: this file needs the following projects to compile:
 * - Apache Commons Codec: http://commons.apache.org/proper/commons-codec/
 * - JSON reference implementation: https://github.com/douglascrockford/JSON-java
 * 
 * @author TeleSign
 *
 */
public class JWTRequestToken {

	/*
	 * Header field keys
	 */
	private static final String KEY_ALG = "alg";
	private static final String KEY_TYP = "typ";

	/*
	 * Claim field keys
	 */
	private static final String KEY_ISS = "iss";
	private static final String KEY_IAT = "iat";
	private static final String KEY_EXP = "exp";
	private static final String KEY_XID = "xid";

	/*
	 * Header field values
	 */
	private static final String HMAC_ALG = "HS256";
	private static final String JWT_TYPE = "JWT";

	/*
	 * String name of HMAC w/ SHA-256 in Java-land.
	 */
	private static final String HMAC_JAVA_ALG = "HmacSHA256";

	/*
	 * Default token validity length of 30 seconds
	 */
	private static final int TOK_VALID_SEC = 30;

	/*
	 * Time that the token is created at. Must be an IntDate ie an integer
	 * timestamp.
	 */
	private final long iat;

	/*
	 * Time that the token expires. Must be in the same format as iat and iat <
	 * exp.
	 */
	private final long exp;

	/*
	 * This is just the CustomerID.
	 */
	private final String iss;

	/*
	 * (Optional). A Customer ReferenceID that will be returned to you by the
	 * TeleSign POST-back.
	 */
	private final String xid;

	/*
	 * API key provided to this object instead of the default.
	 */
	private final String apiKey;

	private String reqToken;

	public JWTRequestToken(String customerID, String apiKey, int timeStart,
			int timeEnd, String exRefID) {
		this.iss = customerID;
		this.iat = timeStart;
		this.exp = timeEnd;
		this.xid = exRefID;
		this.apiKey = apiKey;
	}

	public JWTRequestToken(String customerID, String apiKey, int timeStart,
			int timeEnd) {
		this.iss = customerID;
		this.iat = timeStart;
		this.exp = timeEnd;
		this.xid = null;
		this.apiKey = apiKey;
	}

	public JWTRequestToken(String customerID, String apiKey) {
		this.iss = customerID;
		this.iat = System.currentTimeMillis() / 1000L;
		this.exp = iat + TOK_VALID_SEC;
		this.xid = null;
		this.apiKey = apiKey;
	}

	public String toJWTString() throws NoSuchAlgorithmException,
			InvalidKeyException, UnsupportedEncodingException {

		if (reqToken == null) {

			/*
			 * Build the string from the Header and Claims
			 */
			JSONObject header = new JSONObject();
			JSONObject claims = new JSONObject();

			header.put(KEY_ALG, HMAC_ALG);
			header.put(KEY_TYP, JWT_TYPE);

			claims.put(KEY_IAT, iat);
			claims.put(KEY_EXP, exp);
			claims.put(KEY_ISS, iss);
			if (xid != null) {
				claims.put(KEY_XID, xid);
			}

			StringBuilder builder = new StringBuilder();
			builder.append(encodeBase64URLSafeString(header.toString()
					.getBytes("UTF-8")));
			builder.append(".");
			builder.append(encodeBase64URLSafeString(claims.toString()
					.getBytes("UTF-8")));

			/*
			 * Sign the string using HMAC w/ SHA-256.
			 */
			String signString = builder.toString();
			/*
			 * The TeleSign API key is Base64-encoded, so we have to decode it
			 * first.
			 */
			byte[] decodedApiKey = Base64.decodeBase64(apiKey);

			SecretKey key = new SecretKeySpec(decodedApiKey, HMAC_JAVA_ALG);
			Mac mac;
			mac = Mac.getInstance(HMAC_JAVA_ALG);
			mac.init(key);

			builder.append(".");
			builder.append(encodeBase64URLSafeString(mac.doFinal(signString
					.getBytes())));

			reqToken = builder.toString();

		}

		return reqToken;

	}

	public static void main(String[] args) {
		String customerID = "your_telesign_customer_id";
		String apiKey = "your_telesign_api_key";

		try {
			System.out.print(new JWTRequestToken(customerID, apiKey)
					.toJWTString());
		} catch (InvalidKeyException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
